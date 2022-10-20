pipeline {
  agent any

  stages {
    stage("clone git") {
        steps{
          git 'https://github.com/PhurbaQQ/siteTest.git'
        }
      
    }

    stage("copy site page") {
      steps {
        sh 'cp $JENKINS_HOME/site.html /var/www/html/'
      }
      
    }

    stage("restart nginx") {
      steps {
        sh 'nginx -s reload'
      }
    }
  }
}
