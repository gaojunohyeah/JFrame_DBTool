#!/bin/bash
toolPath='/Users/rayjoy/gaojun/git/JFrame_DBTool'
projectPath='/Users/rayjoy/gaojun/webstrom/JFrame'

daoPath=$projectPath'/app/dao'
managerPath=$projectPath'/app/manager'
modelPath=$projectPath'/app/model'
servicePath=$projectPath'/app/service'

outPath=$toolPath'/out'
outDaoPath=$outPath'/app/dao'
outManagerPath=$outPath'/app/manager'
outModelPath=$outPath'/app/model'
outServicePath=$outPath'/app/service'

#svn update $daoPath'/'
#svn update $managerPath'/'
#svn update $modelPath'/'
#svn update $servicePath'/'
#git pull $toolPath
#git pull $projectPath

python $toolPath'/src/DBBuilder.py'

echo "...................."
echo "copy files, start..."

managerFileList=`ls $outManagerPath`
for managerName in $managerFileList
do
  echo 'managerName='$managerName
  proManagerPath=$managerPath'/'$managerName
  if [ ! -f "$proManagerPath" ]; then
    echo 'copy '$outManagerPath'/'$managerName' to '$proManagerPath
    cp $outManagerPath'/'$managerName $proManagerPath
  else
    echo $proManagerPath' is exist, ignore'
  fi
done

daoFileList=`ls $outDaoPath`
for daoName in $daoFileList
do
  echo 'daoName='$daoName
  proDaoPath=$daoPath'/'$daoName
  if [ ! -f "$proDaoPath" ]; then
    echo 'copy '$outDaoPath'/'$daoName' to '$proDaoPath
    cp $outDaoPath'/'$daoName $proDaoPath
  else
    echo $proDaoPath' is exist, ignore'
  fi
done

echo ''
echo 'copy to '$modelPath
cp $outModelPath'/'*.js  $modelPath'/'

echo ''
echo 'copy to'$servicePath'/manager.js'
cp $outServicePath'/manager.js'  $servicePath'/'

echo ''
echo 'copy to'$servicePath'/dbs.js'
cp $outServicePath'/dbs.js'  $servicePath'/'

echo ''
echo 'copy to'$servicePath'/dao.js'
cp $outServicePath'/dao.js'  $servicePath'/'
echo "copy files, end...."


