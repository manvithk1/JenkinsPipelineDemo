node{
stage('build') {
    // some block
    // example of using arguments to a script
    echo 'Building'
    bat 'cd C:\\Users\\manvi\\DSA-Bootcamp-Java&&dir&&git pull&&git status'
    
    if (currentBuild.result == null || currentBuild.result == 'SUCCESS')
    {
        echo "build stage is successfull"
    }
    else
    {   
        echo "build Stage is not successfull"
    }
}
stage('Pytest') {
    // some block
    // example of using arguments to a script
    echo 'Running python test scripts'
    bat 'cd C:\Jenkins\Src_Code_Git_Folder&&git clone git@github.com:manvithk1/JenkinsPipelineDemo.git'
    bat 'python pyscript.py'
    
    if (currentBuild.result == null || currentBuild.result == 'SUCCESS')
    {
        echo "Pytest stage is successfull"
    }
    else
    {   
        echo "Pytest Stage is not successfull"
    }
    
}
stage('SalinaTests') {
    // some block
    // example of using arguments to a script
    echo 'Running SalinaTests'
    if (currentBuild.result == null || currentBuild.result == 'SUCCESS')
    {
        echo "SalinaTest stage is successfull"
    }
    else
    {   
        echo "SalinaTest Stage is not successfull"
    }
}
}
