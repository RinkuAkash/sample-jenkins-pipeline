pipeline {
	agent any
	
	stages {
		stage('spark-build') {
			steps {
				script {
					sh """
					cd sample-jenkins-pipeline
					/usr/bin/python3 -m venv test-jenkins-env
					test-jenkins-env/Scripts/activate.bat
					/usr/bin/pip3 install -r requirements.txt
					/usr/bin/python3 main.py
					"""
				}
			}
		}
	}
}
