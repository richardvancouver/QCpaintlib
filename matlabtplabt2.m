%%
%{
% data demo
TBD_projectname_xy={};
xx_=[-250000,-250000,250000,250000];
yy_=[-250000,-30000,-30000,-250000];
TBD_projectname_xy{end+1}={xx_,yy_};
xx_=[-250000,-250000,250000,250000];
yy_=[-25000,-15000,-15000,-25000];
TBD_projectname_xy{end+1}={xx_,yy_};
xx_=[-250000,-250000,250000,250000];
yy_=[-10000,10000,10000,-10000];
TBD_projectname_xy{end+1}={xx_,yy_};
xx_=[-250000,-250000,250000,250000];
yy_=[15000,25000,25000,15000];
TBD_projectname_xy{end+1}={xx_,yy_};
xx_=[-250000,-250000,250000,250000];
yy_=[30000,250000,250000,30000];
TBD_projectname_xy{end+1}={xx_,yy_};
TBD_projectname_ports=[[-250000,-20000], [250000,-20000]];
TBD_projectname_boxsize=[500000, 500000];
TBD_projectname_sweep=[4, 8, 2];
project_name_='TBD_projectname';
%}
%CPWs, circuits
TBD_projectname_xy={};
xx_=[-250000,-250000,250000,250000];
yy_=[-250000,-30000,-30000,-250000];
TBD_projectname_xy{end+1}={xx_,yy_};
xx_=[-250000,-250000,250000,250000];
yy_=[-25000,-15000,-15000,-25000];
TBD_projectname_xy{end+1}={xx_,yy_};
xx_=[-250000,-250000,250000,250000];
yy_=[-10000,10000,10000,-10000];
TBD_projectname_xy{end+1}={xx_,yy_};
xx_=[-250000,-250000,250000,250000];
yy_=[15000,25000,25000,15000];
TBD_projectname_xy{end+1}={xx_,yy_};
xx_=[-250000,-250000,250000,250000];
yy_=[30000,250000,250000,30000];
TBD_projectname_xy{end+1}={xx_,yy_};
TBD_projectname_ports=[[-250000,-20000], [250000,-20000]];
TBD_projectname_boxsize=[500000, 500000];
TBD_projectname_sweep=[4, 8, 2];
project_name_='TBD_projectname_mm';


%TBD_projectname_via_xy
TBD_projectname_via_xy={};
xx_=[-250000,-250000,250000,250000];
yy_=[-250000,-30000,-30000,-250000];
TBD_projectname_via_xy{end+1}={xx_,yy_};
% xx_=[-250000,-250000,250000,250000];
% yy_=[-25000,-15000,-15000,-25000];
% TBD_projectname_via_xy{end+1}={xx_,yy_};
% xx_=[-250000,-250000,250000,250000];
% yy_=[-10000,10000,10000,-10000];
% TBD_projectname_via_xy{end+1}={xx_,yy_};
% xx_=[-250000,-250000,250000,250000];
% yy_=[15000,25000,25000,15000];
% TBD_projectname_via_xy{end+1}={xx_,yy_};
% xx_=[-250000,-250000,250000,250000];
% yy_=[30000,250000,250000,30000];
% TBD_projectname_via_xy{end+1}={xx_,yy_};




%TBD_projectname_bridge_xy
TBD_projectname_bridge_xy={};
xx_=[-250000,-250000,250000,250000];
yy_=[-250000,-60000,-60000,-250000];
TBD_projectname_bridge_xy{end+1}={xx_,yy_};
% xx_=[-250000,-250000,250000,250000];
% yy_=[-25000,-15000,-15000,-25000];
% TBD_projectname_bridge_xy{end+1}={xx_,yy_};
% xx_=[-250000,-250000,250000,250000];
% yy_=[-10000,10000,10000,-10000];
% TBD_projectname_bridge_xy{end+1}={xx_,yy_};
% xx_=[-250000,-250000,250000,250000];
% yy_=[15000,25000,25000,15000];
% TBD_projectname_bridge_xy{end+1}={xx_,yy_};
% xx_=[-250000,-250000,250000,250000];
% yy_=[30000,250000,250000,30000];
% TBD_projectname_bridge_xy{end+1}={xx_,yy_};

%=====^ data ^=====v simulate v=====
Project=SonnetProject();
Project.saveAs([project_name_,'.son']);
% length unit
Project.changeLengthUnit('UM');
Project.changeFrequencyUnit('GHZ');
% box size and cell size
unitratio_=0.001;
TBD_projectname_boxsize=TBD_projectname_boxsize*unitratio_;
Project.changeBoxSize(TBD_projectname_boxsize(1),TBD_projectname_boxsize(2));
Project.changeCellSizeUsingNumberOfCells(1,1);
% Set the dielectric layer thicknesses
%Project.changeDielectricLayerThickness(1,50);
%Project.changeDielectricLayerThickness(2,50);
%Project.changeDielectricLayerThickness(3,50);


Project.deleteLayer(1);  %delete the default two layers, 
Project.deleteLayer(1); %two layers are created as soon as you create a .son file
Project.addDielectricLayer('Air',2500,1,1,0,0,0);
Project.addDielectricLayer('Air',2,1,1,0,0,0);
Project.addDielectricLayer('Sapphire',500,9.3,1,3e-006,0,0);






% % Delete the default second layer so we can replace it with a new alumina one
% Project.deleteLayer(2);
% % Add the alumina layer to the Project.
% Project.addDielectricLayer('Alumina',20,9.8,1,1.0e-4,0,0);
%
offset_=TBD_projectname_boxsize/2;
TBD_projectname_polygon={};
for ii = TBD_projectname_xy
    xx_=ii{1}{1}*unitratio_+offset_(1);
    yy_=ii{1}{2}*unitratio_+offset_(2);
    TBD_projectname_polygon{end+1}=Project.addMetalPolygonEasy(1,xx_,yy_);
    Project.changePolygonType(TBD_projectname_polygon{end},'Lossless');
end
Project.openInSonnet();



%add ports to layer 1, do this immediately after setting up polygons in a layer
% TBD_projectname_ports=TBD_projectname_ports*unitratio_;
% portnum_=0;
% for ii = 2:2:size(TBD_projectname_ports,2)
    % portnum_=portnum_+1;
    % Project.addPortAtLocation(TBD_projectname_ports(ii-1)+offset_(1),TBD_projectname_ports(ii)+offset_(2));
% end



%%%%%181115 fixme%%%%%%
%Project.addViaPolygonEasy(0,1,anArrayOfXCoordinates,anArrayOfYCoordinates);
%Project.openInSonnet();

%%%%%
%%add via polygons%%
TBD_projectname_via_polygon={};
for ii = TBD_projectname_via_xy
    xx_=ii{1}{1}*unitratio_+offset_(1);
    yy_=ii{1}{2}*unitratio_+offset_(2);
    TBD_projectname_via_polygon{end+1}=Project.addViaPolygonEasy(1,0,xx_,yy_);
    Project.changePolygonType(TBD_projectname_via_polygon{end},'Lossless');
end
Project.openInSonnet();

%%add bridge polygons%%
TBD_projectname_bridge_polygon={};
for ii = TBD_projectname_bridge_xy
    xx_=ii{1}{1}*unitratio_+offset_(1);
    yy_=ii{1}{2}*unitratio_+offset_(2);
    TBD_projectname_bridge_polygon{end+1}=Project.addMetalPolygonEasy(0,xx_,yy_);
    Project.changePolygonType(TBD_projectname_bridge_polygon{end},'Lossless');
end
Project.openInSonnet();

%
%Abs
%
%Project.addSimpleFrequencySweep(TBD_projectname_sweep(1),TBD_projectname_sweep(2),TBD_projectname_sweep(3));
Project.addAbsFrequencySweep(TBD_projectname_sweep(1),TBD_projectname_sweep(2));
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
	'MET "Unknown_metal" 1 VOL INF 0'},...
    {clines{boxindex}},...
    {...
        '      2000 1 1 0 0 0 0 "Air"',...
		'      2 1 1 0 0 0 0 "Air"',...
        '      500 9.3 1 3e-006 0 0 0 "Sapphire" A 11.5 1 3e-006 0 0 ',...
		'TECHLAY METAL Stream2:2 <UNSPECIFIED> 2 2',...
		'0 0 -1 N 0 1 1 100 100 0 0 0 Y',...
		'END',...
		'END',...
		'TECHLAY VIA Stream3:0 <UNSPECIFIED> 3 0',...
		'VIA POLYGON',...
		'0 0 -1 N 0 1 1 100 100 0 0 0 Y',...
		'TOLEVEL 1 RING NOCOVERS',...
		'END',...
		'END',...
        'TECHLAY METAL Stream10:0 <UNSPECIFIED> 10 0 ',...
        '0 0 0 N 0 1 1 100 100 0 0 0 Y',...
        'END',...
        'END',...
        'LORGN 0 1000 U '...
    },...
    clines{boxindex+4:end}...
);
for ii = boxindex:size(clines,2) %actually boxindex changes now, as cline changes. should be boxindex+2
    if size(clines{ii},2)>=3 && strcmp(clines{ii}(1:3) , 'NUM') %find the beginning
        numindex=ii;
        break
    end
end
insertindexs=[];
insertindexs(end+1)=numindex;
for ii = numindex:size(clines,2)
    if size(clines{ii},2)>=11 && strcmp(clines{ii}(1:11) , 'VIA POLYGON')%find the end  endindex=ii
        break
    end
    if size(clines{ii},2)>=3 && strcmp(clines{ii}(1:3) , 'END')
        insertindexs(end+1)=ii;
    end
end
insertindexs=insertindexs(1:end-1);
templines={};
lastindex=0;
for ii = insertindexs
    templines=cat(2,templines,clines(lastindex+1:ii+1),{'TLAYNAM Stream10:0 INH'}); %keep appending stuff, mainly the end-to-end sections plus 'TLAY...', to templines.
    lastindex=ii+1;
end
clines=cat(2,templines,clines(lastindex+1:end));
%



%%%%%%%%%%%%%%%%%%






%%%%%%%%%%%%%%%%181115 fixme  for via%%%%%%%%%%%%%%%

% for ii = insertindexs
    % templines=cat(2,templines,clines(lastindex+1:ii+1),{'TLAYNAM Stream2:2 INH'});
    % lastindex=ii+1;
% end


%%%%%%%%%%%%%%%%%
for ii = 1:size(clines,2)
    if size(clines{ii},2)>=3 && strcmp(clines{ii}(1:3) , 'NUM')
        boxindex=ii;
        break
    end
end


for ii = boxindex:size(clines,2)
    if size(clines{ii},2)>=7 && strcmp(clines{ii}(1:7) , 'TOLEVEL') %%begining of the insertindex
        beginindex=ii;
        break
    end
end
insertindexs=[];
insertindexs(end+1)=beginindex;
for ii = numindex:size(clines,2)
    if size(clines{ii},2)>=3 && size(clines{ii+1},2)>=3 &&strcmp(clines{ii}(1:3) , 'END') && ~strcmp(clines{ii+1}(1:3) , 'VIA') %%%end of the insertindex find the 'end' with no 'via' following
        endindex=ii;
		break
    end
    if size(clines{ii},2)>=7 && strcmp(clines{ii}(1:7) , 'TOLEVEL')
        insertindexs(end+1)=ii;
    end
end
insertindexs=insertindexs(1:end-1);
templines={};
lastindex=0;
for ii = insertindexs
    templines=cat(2,templines,clines(lastindex+1:ii),{'TLAYNAM Stream3:0 INH'}); %keep appending stuff, mainly the end-to-end sections plus 'TLAY...' to templines.
    lastindex=ii+1;
end
clines=cat(2,templines,clines(lastindex+1:end));






%%%%%%%%%%%%%%%%%%%








%%%%%%%%%%%%%%%%%%181115 fixme  for bridge%%%%%%%%%%%%%

% for ii = insertindexs
    % templines=cat(2,templines,clines(lastindex+1:ii+1),{'TLAYNAM Stream3:0 INH'});
    % lastindex=ii+1;
% end


%%%%%%%%%%%%%%%%%
for ii = 1:size(clines,2)
    if size(clines{ii},2)>=3 && strcmp(clines{ii}(1:3) , 'NUM')
        boxindex=ii;
        break
    end
end


for ii = boxindex:size(clines,2)
    if size(clines{ii},2)>=7 && strcmp(clines{ii}(1:7) , 'TOLEVEL') %%
        numindex=ii;
        break
    end
end
insertindexs=[];
insertindexs(end+1)=numindex;
for ii = numindex:size(clines,2)
    if size(clines{ii},2)>=3 && size(clines{ii+1},2)>=3 && strcmp(clines{ii}(1:3) , 'END') && ~strcmp(clines{ii+1}(1:3) , 'VIA') %%%begining of the insertindex
        beginindex=ii;
		break
    end

end



insertindexs=[];
insertindexs(end+1)=beginindex;
for ii = numindex:size(clines,2)
    if size(clines{ii},2)>=7 && strcmp(clines{ii}(1:7) , 'END GEO') %%%end of the insertindex 
        endindex=ii;
		break
    end
    if size(clines{ii},2)>=3 && strcmp(clines{ii}(1:3) , 'END')
        insertindexs(end+1)=ii;
    end
end
insertindexs=insertindexs(1:end-1);
templines={};
lastindex=0;
for ii = insertindexs
    templines=cat(2,templines,clines(lastindex+1:ii+1),{'TLAYNAM Stream2:2 INH'}); %keep appending stuff, mainly the end-to-end sections plus 'TLAY...' to templines.
    lastindex=ii+1;
end
clines=cat(2,templines,clines(lastindex+1:end));





%%%%%%%%%%%%%%%%%

fid=fopen([project_name_,'.son'],'w');
for ii = 1:size(clines,2)
    fprintf(fid,'%s\n',char(clines{ii}));
end
fclose(fid);
%===================================
%%



