function[freq,s21]=fileread1(ins21)
%fid=fopen('restest2018030813handf0.csv','r');
%fid=fopen('test5.csv','r');
%[array,count]=fscanf(fid,'%f',[col,Inf]);
%fclose(fid);
freq=real(ins21(:,1))'*1e9;
%s21=array(col1,:)+i*array(col2,:);
s21=ins21(:,2)';
%s21=array(col1,:).*cos(array(col2,:)*pi/180)+i*array(col1,:).*sin(array(col2,:)*pi/180);
%array(2,:)

%b=array(2,:);
end
