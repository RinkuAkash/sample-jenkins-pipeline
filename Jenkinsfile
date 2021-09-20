pipeline {
	agent any
	
	stages {
		stage('spark-build') {
			steps {
				script {
					sh """
					cd /home/ubuntu/Downloads/sample-jenkins-pipeline
					python -m venv test-jenkins-env
					test-jenkins-env/Scripts/activate.bat
					pip install -r requirements.txt
					python main.py
					"""
				}
			}
		}
	}
}
