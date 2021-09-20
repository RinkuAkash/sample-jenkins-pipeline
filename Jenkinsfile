pipeline {
        agent any

        stages {
                stage('spark-build') {
                        steps {
                                script {
                                        sh """
                                        git clone https://github.com/RinkuAkash/sample-jenkins-pipeline.git
                                        cd sample-jenkins-pipeline
                                        pip install -r requirements.txt
                                        python main.py
                                        python test/testMain.py
                                        """
                                }
                        }
                }
        }
}
