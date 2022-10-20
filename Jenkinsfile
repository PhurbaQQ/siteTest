pipeline {
  agent any

  stages {
    stage("copy site page") {
      steps {
        sh 'cp $JENKINS_HOME/workspace/Test_main/index.html /var/www/html/'
      }
      
    }

    stage("restart nginx") {
      steps {
        sh 'nginx -s reload'
      }
    }
  }
}
