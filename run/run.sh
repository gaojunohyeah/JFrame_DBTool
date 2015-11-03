#!/bin/bash
toolPath='/Users/rayjoy/gaojun/work/tank2/docs/技术工具/DBBuilderTool'
projectPath='/Users/rayjoy/gaojun/work/tank2server/game/tank-luascripts'

cfgPath=$toolPath'/config'
managerPath=$projectPath'/game/manager'
modelPath=$projectPath'/game/model'
servicePath=$projectPath'/mvc'

outPath=$toolPath'/out'
outManagerPath=$outPath'/game/manager'
outModelPath=$outPath'/game/model'
outServicePath=$outPath'/mvc'

svn update $cfgPath'/'
svn update $managerPath'/'
svn update $modelPath'/'
svn update $servicePath'/'

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

echo ''
echo 'copy to '$modelPath
cp $outModelPath'/'*.lua  $modelPath'/'

echo ''
echo 'copy to'$servicePath'/ManagerServicesAuto.lua'
cp $outServicePath'/ManagerServicesAuto.lua'  $servicePath'/'

echo ''
echo 'copy to'$servicePath'/ModelNames.lua'
cp $outServicePath'/ModelNames.lua'  $servicePath'/'
echo "copy files, end...."


