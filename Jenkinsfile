pipeline {
	agent any
	
	stages {
		stage('spark-build') {
			steps {
				script {
					sh """
					rm -r sample-jenkins-pipeline
					git clone https://github.com/RinkuAkash/sample-jenkins-pipeline.git
					sudo apt-get install python-is-python3
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
