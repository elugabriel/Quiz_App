# routes.py - Add these endpoints

from flask import jsonify, request
from sqlalchemy import or_

# Get all available modules
@app.route('/api/modules', methods=['GET'])
def get_modules():
    modules = db.session.query(Question.topic).distinct().all()
    modules_list = [module[0] for module in modules]
    
    # Organize by category
    organized_modules = {
        "Computer Hardware": [m for m in modules_list if m.startswith("Computer Hardware")],
        "Computer Ports": [m for m in modules_list if "Ports" in m],
        "Software": [m for m in modules_list if m.startswith("Software")],
        "Phone Repair": [m for m in modules_list if m.startswith("Phone Repair")],
        "Hardware Functions": [m for m in modules_list if m.startswith("Hardware Functions")],
        "GSM Repair": [m for m in modules_list if m.startswith("GSM Repair")]
    }
    
    return jsonify({
        "success": True,
        "modules": organized_modules
    })

# Get questions by module (with pagination)
@app.route('/api/modules/<module_name>/questions', methods=['GET'])
def get_module_questions(module_name):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    # Decode module name from URL
    module_name = module_name.replace('_', ' ')
    
    pagination = Question.query.filter_by(topic=module_name).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    questions = [{
        'id': q.id,
        'topic': q.topic,
        'q_type': q.q_type,
        'prompt': q.prompt,
        'options': q.options.split(',') if isinstance(q.options, str) else q.options,
        'difficulty': q.difficulty,
        'image_path': q.image_path
    } for q in pagination.items]
    
    return jsonify({
        'success': True,
        'module': module_name,
        'total': pagination.total,
        'page': page,
        'per_page': per_page,
        'pages': pagination.pages,
        'questions': questions
    })

# Get module progress for a user
@app.route('/api/modules/<module_name>/progress', methods=['GET'])
def get_module_progress(module_name):
    user_id = request.args.get('user_id')  # Assuming you have user authentication
    
    total_questions = Question.query.filter_by(topic=module_name).count()
    
    # Assuming you have a UserAnswer model tracking answers
    # completed = UserAnswer.query.filter_by(user_id=user_id, topic=module_name, correct=True).count()
    
    # Placeholder progress
    completed = 0
    
    return jsonify({
        'module': module_name,
        'total_questions': total_questions,
        'completed': completed,
        'percentage': (completed / total_questions * 100) if total_questions > 0 else 0
    })

# Get module summary (all questions with user's answers)
@app.route('/api/modules/<module_name>/summary', methods=['GET'])
def get_module_summary(module_name):
    user_id = request.args.get('user_id')
    
    questions = Question.query.filter_by(topic=module_name).all()
    
    # Group by sub-topic
    grouped = {}
    for q in questions:
        sub_topic = q.topic.split(' - ')[-1] if ' - ' in q.topic else 'General'
        if sub_topic not in grouped:
            grouped[sub_topic] = []
        
        # Get user's answer if exists
        # user_answer = UserAnswer.query.filter_by(user_id=user_id, question_id=q.id).first()
        
        grouped[sub_topic].append({
            'id': q.id,
            'type': q.q_type,
            'prompt': q.prompt,
            'difficulty': q.difficulty,
            # 'user_answer': user_answer.answer if user_answer else None,
            # 'is_correct': user_answer.correct if user_answer else None
        })
    
    return jsonify({
        'module': module_name,
        'sub_modules': grouped,
        'total_questions': len(questions)
    })