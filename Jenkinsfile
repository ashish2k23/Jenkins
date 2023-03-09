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
		bat (script: "python_functions.py 'Ashish',40").trim()
      }
    }
  }
}

