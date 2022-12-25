node{
stage('build') {
    // some block
    // example of using arguments to a script
    echo 'Building'
    bat 'cd C:\\Users\\manvi\\DSA-Bootcamp-Java&&dir&&git pull&&git status'
}
stage('Pytest') {
    // some block
    // example of using arguments to a script
    echo 'Running python test scripts'
    bat 'cd C:\Jenkins\Src_Code_Git_Folder&&git clone git@github.com:manvithk1/JenkinsPipelineDemo.git'
    bat 'python pyscript.py'
    
}
stage('SalinaTests') {
    // some block
    // example of using arguments to a script
    echo 'Running SalinaTests'
}
}
