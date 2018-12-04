testbrick_xy={};
xx_=[-71000,-71000,71000,71000,-42500,-42500,-37500,-37500,71000,71000,28318,28318,42358,42358,49918,49918,65038,65038,32638,32638,60718,60718,54238,54238,38038,38038,28318,28318,71000,71000];
yy_=[-112500,112500,112500,102000,102000,98000,98000,102000,102000,87255,87255,78615,78615,-87705,-87705,78615,78615,-102825,-102825,-98505,-98505,74295,74295,-92025,-92025,74295,74295,-111465,-111465,-112500];
testbrick_xy{end+1}={xx_,yy_};
testbrick_via_xy={};
xx_=[-44040,-44040,-42124,-42124];
yy_=[98000,102000,102000,98000];
testbrick_via_xy{end+1}={xx_,yy_};
xx_=[-38010,-38010,-36010,-36010];
yy_=[98000,102000,102000,98000];
testbrick_via_xy{end+1}={xx_,yy_};
testbrick_bridge_xy={};
xx_=[-60242,-60242,28318,28318,36958,36958];
yy_=[-102825,78615,78615,-98505,-98505,-102825];
testbrick_bridge_xy{end+1}={xx_,yy_};
xx_=[-26740,-26740,-22540,-22540];
yy_=[86000,103000,103000,86000];
testbrick_bridge_xy{end+1}={xx_,yy_};
xx_=[-56040,-56040,-49040,-49040];
yy_=[91000,109000,109000,91000];
testbrick_bridge_xy{end+1}={xx_,yy_};
xx_=[-32340,-32340,-30040,-30040];
yy_=[91000,109000,109000,91000];
testbrick_bridge_xy{end+1}={xx_,yy_};
testbrick_brick_xy={};
xx_=[-68882,-68882,32638,32638];
yy_=[-111465,87255,87255,-111465];
testbrick_brick_xy{end+1}={xx_,yy_};
xx_=[-59040,-59040,-46040,-46040];
yy_=[94000,106000,106000,94000];
testbrick_brick_xy{end+1}={xx_,yy_};
xx_=[-29040,-29040,-34540,-34540,-20541,-20541];
yy_=[90000,94000,94000,106000,106000,90000];
testbrick_brick_xy{end+1}={xx_,yy_};
testbrick_ports=[[0.0, -110000.0], [0.0, 110000.0]];
testbrick_boxsize=[142000, 225000];
testbrick_sweep=[4, 8, 0.006666666666666667];
project_name_='testbrick';
%%
%{
% data demo
testbrick_xy={};
xx_=[-250000,-250000,250000,250000];
yy_=[-250000,-30000,-30000,-250000];
testbrick_xy{end+1}={xx_,yy_};
xx_=[-250000,-250000,250000,250000];
yy_=[-25000,-15000,-15000,-25000];
testbrick_xy{end+1}={xx_,yy_};
xx_=[-250000,-250000,250000,250000];
yy_=[-10000,10000,10000,-10000];
testbrick_xy{end+1}={xx_,yy_};
xx_=[-250000,-250000,250000,250000];
yy_=[15000,25000,25000,15000];
testbrick_xy{end+1}={xx_,yy_};
xx_=[-250000,-250000,250000,250000];
yy_=[30000,250000,250000,30000];
testbrick_xy{end+1}={xx_,yy_};
testbrick_ports=[[-250000,-20000], [250000,-20000]];
testbrick_boxsize=[500000, 500000];
testbrick_sweep=[4, 8, 2];
project_name_='testbrick';
%}
%CPWs, circuits
% testbrick_xy={};
% xx_=[-250000,-250000,250000,250000];
% yy_=[-250000,-30000,-30000,-250000];
% testbrick_xy{end+1}={xx_,yy_};
% xx_=[-250000,-250000,250000,250000];
% yy_=[-25000,-15000,-15000,-25000];
% testbrick_xy{end+1}={xx_,yy_};
% xx_=[-250000,-250000,250000,250000];
% yy_=[-10000,10000,10000,-10000];
% testbrick_xy{end+1}={xx_,yy_};
% xx_=[-250000,-250000,250000,250000];
% yy_=[15000,25000,25000,15000];
% testbrick_xy{end+1}={xx_,yy_};
% xx_=[-250000,-250000,250000,250000];
% yy_=[30000,250000,250000,30000];
% testbrick_xy{end+1}={xx_,yy_};
% testbrick_ports=[[-250000,-20000], [250000,-20000]];
% testbrick_boxsize=[500000, 500000];
% testbrick_sweep=[4, 8, 2];
% project_name_='testbrick_mmbricviac';
%%
%%
%testbrick_via_xy
% testbrick_via_xy={};
% xx_=[-250000,-250000,250000,250000]/2;
% yy_=[-250000,-30000,-30000,-250000]/2;
% testbrick_via_xy{end+1}={xx_,yy_};
% xx_=[-250000,-250000,250000,250000];
% yy_=[-25000,-15000,-15000,-25000];
% testbrick_via_xy{end+1}={xx_,yy_};
% xx_=[-250000,-250000,250000,250000];
% yy_=[-10000,10000,10000,-10000];
% testbrick_via_xy{end+1}={xx_,yy_};
% xx_=[-250000,-250000,250000,250000];
% yy_=[15000,25000,25000,15000];
% testbrick_via_xy{end+1}={xx_,yy_};
% xx_=[-250000,-250000,250000,250000];
% yy_=[30000,250000,250000,30000];
% testbrick_via_xy{end+1}={xx_,yy_};

%%

%testbrick_brick_xy
% testbrick_brick_xy={};
% xx_=[-250000,-250000,250000,250000];
% yy_=[-250000,-30000,-30000,-250000];
% testbrick_brick_xy{end+1}={xx_,yy_};


%%
%%
%%
%%
%%
%testbrick_bridge_xy
% testbrick_bridge_xy={};
% xx_=[-250000,-250000,250000,250000];
% yy_=[-250000,-60000,-60000,-250000];
% testbrick_bridge_xy{end+1}={xx_,yy_};
% xx_=[-250000,-250000,250000,250000];
% yy_=[-25000,-15000,-15000,-25000];
% testbrick_bridge_xy{end+1}={xx_,yy_};
% xx_=[-250000,-250000,250000,250000];
% yy_=[-10000,10000,10000,-10000];
% testbrick_bridge_xy{end+1}={xx_,yy_};
% xx_=[-250000,-250000,250000,250000];
% yy_=[15000,25000,25000,15000];
% testbrick_bridge_xy{end+1}={xx_,yy_};
% xx_=[-250000,-250000,250000,250000];
% yy_=[30000,250000,250000,30000];
% testbrick_bridge_xy{end+1}={xx_,yy_};
%%
%=====^ data ^=====v simulate v=====
Project=SonnetProject();
Project.saveAs([project_name_,'.son']);
% length unit
Project.changeLengthUnit('UM');
Project.changeFrequencyUnit('GHZ');
% box size and cell size
unitratio_=0.001;
testbrick_boxsize=testbrick_boxsize*unitratio_;
Project.changeBoxSize(testbrick_boxsize(1),testbrick_boxsize(2));
Project.changeCellSizeUsingNumberOfCells(1,1);
% Set the dielectric layer thicknesses
%Project.changeDielectricLayerThickness(1,50);
%Project.changeDielectricLayerThickness(2,50);
%Project.changeDielectricLayerThickness(3,50);


Project.deleteLayer(1);  %delete the default two layers, 
Project.deleteLayer(1); %two layers are created as soon as you create a .son file
Project.addDielectricLayer('Air',2500,1,1,0,0,0);
Project.addDielectricLayer('Air',2,1,1,0,0,0);%Project.addBrickTechLayer('Air',2,1,1,0,0,0); need to add the 7th para, Zpartition=1 in the clines part
Project.addDielectricLayer('Sapphire',500,9.3,1,3e-006,0,0);






% % Delete the default second layer so we can replace it with a new alumina one
% Project.deleteLayer(2);
% % Add the alumina layer to the Project.
% Project.addDielectricLayer('Alumina',20,9.8,1,1.0e-4,0,0);
%
offset_=testbrick_boxsize/2;
testbrick_polygon={};
for ii = testbrick_xy
    xx_=ii{1}{1}*unitratio_+offset_(1);
    yy_=ii{1}{2}*unitratio_+offset_(2);
    testbrick_polygon{end+1}=Project.addMetalPolygonEasy(1,xx_,yy_);
    Project.changePolygonType(testbrick_polygon{end},'Lossless');
end
Project.openInSonnet();



%add ports to layer 1, do this immediately after setting up polygons in a layer
testbrick_ports=testbrick_ports*unitratio_;
portnum_=0;
for ii = 2:2:size(testbrick_ports,2)
    portnum_=portnum_+1;
    Project.addPortAtLocation(testbrick_ports(ii-1)+offset_(1),testbrick_ports(ii)+offset_(2));
end




%%%%%181115 fixme%%%%%%
%Project.addViaPolygonEasy(0,1,anArrayOfXCoordinates,anArrayOfYCoordinates);
%Project.openInSonnet();

%%add via polygons%%
testbrick_via_polygon={};
for ii = testbrick_via_xy
    xx_=ii{1}{1}*unitratio_+offset_(1);
    yy_=ii{1}{2}*unitratio_+offset_(2);
    testbrick_via_polygon{end+1}=Project.addViaPolygonEasy(1,0,xx_,yy_);
    Project.changePolygonType(testbrick_via_polygon{end},'Lossless');
end
Project.openInSonnet();

%%%%%
%%add brick polygons%%
testbrick_brick_polygon={};
for ii = testbrick_brick_xy
    xx_=ii{1}{1}*unitratio_+offset_(1);
    yy_=ii{1}{2}*unitratio_+offset_(2);
    testbrick_brick_polygon{end+1}=Project.addDielectricBrickEasy(1,xx_,yy_);  %try addDielectricBrickEasy .addDielectricBrickEasy(0,[5,10,10,5,5],[10,10,20,20,10],'Brick1')
    %Project.changePolygonType(testbrick_via_polygon{end},'Lossless');
end
Project.openInSonnet();







%%add bridge polygons%%
testbrick_bridge_polygon={};
for ii = testbrick_bridge_xy
    xx_=ii{1}{1}*unitratio_+offset_(1);
    yy_=ii{1}{2}*unitratio_+offset_(2);
    testbrick_bridge_polygon{end+1}=Project.addMetalPolygonEasy(0,xx_,yy_);
    Project.changePolygonType(testbrick_bridge_polygon{end},'Lossless');
end
Project.openInSonnet();

%
%Abs
%
%Project.addSimpleFrequencySweep(testbrick_sweep(1),testbrick_sweep(2),testbrick_sweep(3));
Project.addAbsFrequencySweep(testbrick_sweep(1),testbrick_sweep(2));
Project.ControlBlock.TargetAbs=5000;
% Add an output file and then resimulate
Project.addTouchstoneOutput;
% Project.openInSonnet();
Project.saveAs([project_name_,'.son']);
%===================================
%%
%%
fid=fopen([project_name_,'.son'],'r');
str=fread(fid);
fclose(fid);
str=char(str');
lines=strsplit(str,sprintf('\n'));
clines=lines;
for ii = 1:size(clines,2)
    if strcmp(clines{ii}(1:3) , 'BOX')
        boxindex=ii;
        break
    end
end
clines=cat(2,...
	{clines{1}},...
	{'VER 14.52'},...
    clines{3:boxindex-1},...
    {'MET "Al" 1 NOR INF 0 0.1 ',...
	'MET "Unknown_metal" 1 VOL INF 0',...
    'BRI "Stream3:0" 1 5 0 0'},... %%added this BRI line 2 1 1 0.  2 5 0 0 gives Stream3:0 option, epsilon=5
    {clines{boxindex}},...
    {...
        '      2000 1 1 0 0 0 1 "Air"',...
		'      2 1 1 0 0 0 1 "Air"',...
        '      500 9.3 1 3e-006 0 0 0 "Sapphire" A 11.5 1 3e-006 0 0 ',...
		'TECHLAY METAL Stream2:2 <UNSPECIFIED> 2 2',...%Tech metal 0 0 0, 3rd digit sets material
		'0 0 0 N 0 1 1 100 100 0 0 0 Y',...
		'END',...
		'END',...
        'TECHLAY VIA Stream3:0 <UNSPECIFIED> 3 0',...
		'VIA POLYGON',...
		'0 0 -1 N 0 1 1 100 100 0 0 0 Y',...
		'TOLEVEL 1 RING NOCOVERS',...
		'END',...
		'END',...
		'TECHLAY BRICK Stream3:0 <UNSPECIFIED> 3 0',...
		'BRI POLY',...
		'1 0 1 N 0 1 1 100 100 0 0 0 Y',... %%change via to brick, 1 0 0, not 1 0 -1; 1 0 1, the 3rd 1 indicates material 
		'END',...
		'END',...
        'TECHLAY METAL Stream10:0 <UNSPECIFIED> 10 0',...
        '1 0 0 N 0 1 1 100 100 0 0 0 Y',...
        'END',...
        'END',...
        'LORGN 0 1000 U '...
    },...
    clines{boxindex+4:end}...
);


fid=fopen([project_name_,'.son'],'w');
for ii = 1:size(clines,2)
    fprintf(fid,'%s\n',char(clines{ii}));
end
fclose(fid);
%%It seems that runs until here is enough, no need to add TechLayer
%%senetnces with the following code. Sonnet can recognize the layer
%%correspondence automatically, based on their order of showing up. 
%%Because the first digit already indicates the layer, no need to insert the
%%'TLAYNAM Stream' information
%%
% for ii = boxindex:size(clines,2) %actually boxindex changes now, as cline changes. should be boxindex+2
%     if size(clines{ii},2)>=3 && strcmp(clines{ii}(1:3) , 'NUM') %find the beginning
%         numindex=ii;
%         break
%     end
% end
% insertindexs=[];
% insertindexs(end+1)=numindex;
% for ii = numindex:size(clines,2)
%     if size(clines{ii},2)>=8 && strcmp(clines{ii}(1:8) , 'BRI POLY')%find the end  endindex=ii
%         break
%     end
%     if size(clines{ii},2)>=3 && strcmp(clines{ii}(1:3) , 'END')
%         insertindexs(end+1)=ii;
%     end
% end
% insertindexs=insertindexs(1:end-1);
% templines={};
% lastindex=0;
% for ii = insertindexs
%     templines=cat(2,templines,clines(lastindex+1:ii+1),{'TLAYNAM Stream10:0 NOH'}); %keep appending stuff, mainly the end-to-end sections plus 'TLAY...', to templines.
%     lastindex=ii+1;
% end
% clines=cat(2,templines,clines(lastindex+1:end));
% %%
% 
% 
% 
% %%%%%%%%%%%%%%%%%%
% 
% fid=fopen([project_name_,'.son'],'w');
% for ii = 1:size(clines,2)
%     fprintf(fid,'%s\n',char(clines{ii}));
% end
% fclose(fid);


%%


%%%%%%%%%%%%%%%%181115 fixme  for via%%%%%%%%%%%%%%%

% for ii = insertindexs
    % templines=cat(2,templines,clines(lastindex+1:ii+1),{'TLAYNAM Stream2:2 INH'});
    % lastindex=ii+1;
% end


% %%%%%%%%%%%%%%%%%
% for ii = 1:size(clines,2)
%     if size(clines{ii},2)>=3 && strcmp(clines{ii}(1:3) , 'NUM')
%         boxindex=ii;
%         break
%     end
% end
% % %newboxindex=boxindex
% % 
% for ii = boxindex:size(clines,2)
%     if size(clines{ii},2)>=8 && strcmp(clines{ii}(1:8) , 'BRI POLY') %%begining of the insertindex
%         beginindex=ii;
%         break
%     end
% end
% %beginindex
% insertindexs=[];
% insertindexs(end+1)=beginindex+1;
% % %insertindexs
% for ii = beginindex:size(clines,2)
%     if size(clines{ii},2)>=3 && size(clines{ii+1},2)>=8 &&strcmp(clines{ii}(1:3) , 'END') && ~strcmp(clines{ii+1}(1:8) , 'BRI POLY') %%%end of the insertindex find the 'end' with no 'via' following
%         endindex=ii;
% 		break
%     end
%     if size(clines{ii},2)>=8 && strcmp(clines{ii}(1:8) , 'BRI POLY')
%         insertindexs(end+1)=ii+1;
%     end
% end
% % %insertindexs
% insertindexs=insertindexs(1:end-1);
% % %afterendm1=insertindexs
% templines={};
% lastindex=0;
% for ii = insertindexs
%     templines=cat(2,templines,clines(lastindex+1:ii),{'TLAYNAM Stream3:0 NOH'}); %keep appending stuff, mainly the end-to-end sections plus 'TLAY...' to templines.
%     lastindex=ii+1;
% end
% clines=cat(2,templines,clines(lastindex+1:end));
% 
% 
% 
% 
% %%
% 
% %%%%%%%%%%%%%%%%%%%
% 
% 
% %%%%%%%%%%%%%%%%%%
% % 
% fid=fopen([project_name_,'.son'],'w');
% for ii = 1:size(clines,2)
%     fprintf(fid,'%s\n',char(clines{ii}));
% end
% fclose(fid);
%%




%%%%%%%%%%%%%%%%%%181115 fixme  for bridge%%%%%%%%%%%%%

% for ii = insertindexs
    % templines=cat(2,templines,clines(lastindex+1:ii+1),{'TLAYNAM Stream3:0 INH'});
    % lastindex=ii+1;
% end


%%%%%%%%%%%%%%%%
% for ii = 1:size(clines,2)
%     if size(clines{ii},2)>=3 && strcmp(clines{ii}(1:3) , 'NUM')
%         boxindex=ii;
%         break
%     end
% end
% %bridgeboxindex=boxindex
% 
% for ii = boxindex:size(clines,2)
%     if size(clines{ii},2)>=8 && strcmp(clines{ii}(1:8) , 'BRI POLY') %%
%         numindex=ii;
%         break
%     end
% end
% %bridgenum=numindex
% insertindexs=[];
% insertindexs(end+1)=numindex;
% for ii = numindex:size(clines,2)
%     if size(clines{ii},2)>=3 && size(clines{ii+1},2)>=8 && strcmp(clines{ii}(1:3) , 'END') && ~strcmp(clines{ii+1}(1:8) , 'BRI POLY') %%%begining of the insertindex
%         beginindex=ii;
% 		break
%     end
% 
% end
% 
% %bridgebeginindex=beginindex
% 
% insertindexs=[];
% insertindexs(end+1)=beginindex;
% 
% %bridgeinsertindexs=insertindexs
% for ii = beginindex+1:size(clines,2)
%     if size(clines{ii},2)>=7 && strcmp(clines{ii}(1:7) , 'END GEO') %%%end of the insertindex 
%         endindex=ii;
% 		break
%     end
%     if size(clines{ii},2)>=3 && strcmp(clines{ii}(1:3) , 'END')
%         insertindexs(end+1)=ii;
%     end
% end
% %bridgeendindex=endindex
% insertindexs=insertindexs(1:end-1);
% %bridgeinsertindexs=insertindexs
% templines={};
% lastindex=0;
% for ii = insertindexs
%     templines=cat(2,templines,clines(lastindex+1:ii+1),{'TLAYNAM Stream2:2 NOH'}); %keep appending stuff, mainly the end-to-end sections plus 'TLAY...' to templines.
%     lastindex=ii+1;
% end
% clines=cat(2,templines,clines(lastindex+1:end));
% 
% 
% 
% 
% 
% %%%%%%%%%%%%%%%%%
% 
% fid=fopen([project_name_,'.son'],'w');
% for ii = 1:size(clines,2)
%     fprintf(fid,'%s\n',char(clines{ii}));
% end
% fclose(fid);
%===================================
%%
%%simulation and fit module%%
%===================================
%%
Project=SonnetProject([project_name_,'.son']);
testbrick_Project=Project;
Project.simulate('-c');
% Read Touchstone Output File for S11 and S21
snpfilename_=[project_name_,'.s',num2str(portnum_),'p'];
S11 = TouchstoneParser(snpfilename_,1,1);
S21 = TouchstoneParser(snpfilename_,2,1);
% Convert the S11 and S21 data to dB
S11dB = 20*log10(abs(S11(:,2)));
S21dB = 20*log10(abs(S21(:,2)));
% Plot S11 and S21 data in dB
F = S11(:,1);
%plot(F,S11dB,F,S21dB);
%title('dB(S_2_1) and dB(S_1_1) vs Freq.');
%xlabel('F [GHz]');
%ylabel('dB(S)');
%legend('dB(S_1_1)','dB(S_2_1)','Location','Best')
%grid on

%[c,dc] = qfit1(S21)

% save(  strcat(project_name_,'.mat'),'c','dc' )
%
% Project.viewResponseData();

% output=6.093; % real freq

[~,index]=min(S21dB);
output=F(index);



