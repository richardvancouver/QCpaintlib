c=[1,2,3,4]
project_name_='testb'
save(  strcat(project_name_,'.mat'),'c'  )

assignin('base', strcat( project_name_,num2str(3)), c); %successfully rename c, rename it as strcat( project_name_, num2str(3)) 

fid=fopen([project_name_,'.mat'],'r')
dd=3
if (fid==-1)
    tt=33
save(  strcat(project_name_,'.mat'),'c'  )

else
    dd    
   save(  strcat(project_name_,'.mat'),strcat( project_name_,num2str(3)) ,'-append' )
end

fclose(fid);
