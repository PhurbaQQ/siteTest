pipeline {
  agent any

  stages {
    stage("clone git") {
        steps{
          git credentialsId: 'GitHub', url: 'https://github.com/PhurbaQQ/siteTest.git'
        }
      
    }
    stage("find file") {
      steps {
        fileExists './site.html'
      }
    }

    stage("copy site page") {
      steps {
        sh 'cp $JENKINS_HOME/workspace/Test_main/site.html /var/www/html/'
      }
      
    }

    stage("restart nginx") {
      steps {
        sh 'nginx -s reload'
      }
    }
  }
}
