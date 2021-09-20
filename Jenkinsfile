pipeline {
	agent {
		docker	{
			image "python:3.8.12"
		}
	}
	
	stages {
		stage('spark-build') {
			steps {
				script {
					sh """
					cd sample-jenkins-pipeline
					python3 -m venv test-jenkins-env
					test-jenkins-env/Scripts/activate.bat
					pip3 install -r requirements.txt
					python3 main.py
					"""
				}
			}
		}
	}
}
