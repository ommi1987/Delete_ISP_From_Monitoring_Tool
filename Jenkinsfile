pipeline {
    agent any

    environment {
        GIT_CRED = credentials('ef4fcb76-64f0-4cf0-af29-16e94c03fcd4')  // ID you saved in Jenkins
    }

    parameters {
        string(name: 'ISP_NAME', defaultValue: '', description: 'Mandatory! Enter ISP Name Configured In Monitoring Tool To Delete..!')
        //string(name: 'ISP_PUBLIC_IP', defaultValue: '', description: 'Mandatory! Enter ISP Public IP (e.g. 1.2.3.4)')
    }

    stages {
        
    stage('Install Dependencies') {
    steps {
        sh '''
        python3 -m venv venv
        . venv/bin/activate
        pip install --upgrade pip
        pip install -r requirements.txt
        '''
        }
    }

    stage('Run Python Script') {
    steps {
        withCredentials([usernamePassword(credentialsId: 'ef4fcb76-64f0-4cf0-af29-16e94c03fcd4',
                                          usernameVariable: 'GITHUB_USER',
                                          passwordVariable: 'GITHUB_PASS')]) {
            sh '''
                . venv/bin/activate
                ISP_CLEANED=$(echo "${ISP_NAME}" | xargs)
                echo "Passing ISP name: [$ISP_CLEANED]"
                python3 delete_monitor.py "$ISP_CLEANED"
                   
                    
            '''
                }
            }
        }
    }
}
