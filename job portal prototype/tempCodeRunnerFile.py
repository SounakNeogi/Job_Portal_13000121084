@app.route('/search_job_description', methods=['POST'])
def search_job_description():
    job_data = request.get_json()
    job_description = job_data.get('job_description')
    print(job_description)
    client = MongoClient('mongodb://localhost:27017/')
    db = client['myDatabase']  # Replace 'myDatabase' with your actual database name
    collection = db['job_data']

    # Search the MongoDB collection for the job description
    # Adjust the search query based on your MongoDB schema and how you store job descriptions
    result = collection.find({'job': job_description}, {'_id':False})
    data=[]
    for item in result:
        data.append([item['job'],item['company']])
    print(data)
    return jsonify({'result': data})