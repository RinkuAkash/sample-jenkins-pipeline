pipeline {
	agent any
	
	stages {
		stage('spark-build') {
			steps {
				script {
					sh """
					git clone https://github.com/RinkuAkash/sample-jenkins-pipeline.git
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
