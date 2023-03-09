pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python --version'
      }
    }
    stage('hello') {
      steps {
        bat 'python hello.py'
		bat (script: "python python_functions.py 'Ashish'")
      }
    }
  }
}

