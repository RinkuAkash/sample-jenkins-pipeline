pipeline {
        agent any

        stages {
                stage('spark-build') {
                        steps {
                                script {
                                        sh """
                                        cd /home/ubuntu/Downloads/sample-jenkins-pipeline
                                        pip install -r requirements.txt
                                        python main.py
                                        python test/testMain.py
                                        """
                                }
                        }
                }
        }
}
