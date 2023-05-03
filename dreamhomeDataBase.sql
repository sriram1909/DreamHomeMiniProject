create database if not exists dreamhomefinal;
use dreamhomefinal;

-- branch details which are to be included
show tables;
CREATE TABLE branch
(branchNo char(5) PRIMARY KEY,
 street varchar(35),
 city varchar(10) not null,
 postcode varchar(10) not null,
 telNo numeric(20) not null,
 supervisor_staffNo varchar(20),
 manager_staffNo char(10)
);

INSERT INTO branch VALUES('B005','22 Deer Rd','London','SW1 4EH',0403355755,null,'SL21');
INSERT INTO branch VALUES('B007','16 Argyll St', 'Aberdeen','AB2 3SU',0403355777,null,null);
INSERT INTO branch VALUES('B004','32 Manse Rd', 'Bristol','BS99 1NZ',0403355744,null,null);
INSERT INTO branch VALUES('B003','163 Main St', 'Glasgow','G11 9QX',0403355733,'SG14','SG5');
INSERT INTO branch VALUES('B002','56 Clover Dr', 'London','NW10 6EU',0403355722,null,null);

-- details of staff who joined
CREATE TABLE staff
(staffNo char(5) PRIMARY KEY,
 fName varchar(20),
 position varchar(10),
 sex char(1),
 telephone varchar(15),
 DOB date,
 salary int,
 branchNo char(5),
 foreign key (branchNo) references branch(branchNo)
);

desc staff;

INSERT INTO staff VALUES('SL21','John White','Manager','M','123456789','1965-10-01',30000,'B005');
INSERT INTO staff VALUES('SG37','Ann Beech','Assistant','F','987654321','1980-11-10',12000,'B003');
INSERT INTO staff VALUES('SB14','David Ford','Supervisor','M','3334455555','1978-03-24',18000,'B002');
INSERT INTO staff VALUES('SA9','Mary Howe','Assistant','F','6547893213','1990-02-19',9000,'B007');
INSERT INTO staff VALUES('SG5','Susan Brand','Manager','F','4567891230','1960-06-03',24000,'B003');
INSERT INTO staff VALUES('SL41','Julie Lee','Assistant','F','9517532580','1985-06-13',9000,'B005');

-- details of the owner who want to rent out property
CREATE TABLE privateOwner
(ownerNo char(5) PRIMARY KEY,
 fName varchar(20),
 address varchar(50),
 telNo char(15),
 email varchar(50),
 password varchar(40)
);

INSERT INTO privateOwner VALUES('CO46','Joe Keogh','2 Fergus Dr. Aberdeen AB2 ','01224-861212', 'jkeogh@lhh.com', null);
INSERT INTO privateOwner VALUES('CO87','Carol Farrel','6 Achray St. Glasgow G32 9DX','0141-357-7419', 'cfarrel@gmail.com', null);
INSERT INTO privateOwner VALUES('CO40','Tina Murphy','63 Well St. Glasgow G42','0141-943-1728', 'tinam@hotmail.com', null);
INSERT INTO privateOwner VALUES('CO93','Tony Shaw','12 Park Pl. Glasgow G4 0QR','0141-225-7025', 'tony.shaw@ark.com', null);

-- properties available to rent out 

drop table if exists propertyForRent;
CREATE TABLE propertyForRent
(propertyNo char(5) PRIMARY KEY,
 street varchar(35),
 city varchar(10),
 postcode varchar(10),
 type varchar(10),
 rooms smallint,
 rent int,
 ownerNo char(5) not null,
 staffNo char(5),
 branchNo char(5),
 foreign key(branchNo) references branch(branchNo),
 foreign key(ownerNo) references privateowner(ownerNo),
 foreign key(staffNo) references staff(staffNo)
);

-- alter table propertyforrent add column rentstatus bool;

INSERT INTO propertyForRent VALUES('PA14','16 Holhead','Aberdeen','AB7 5SU','House',6,650,'CO46','SA9','B007');
INSERT INTO propertyForRent VALUES('PL94','6 Argyll St','London','NW2','Flat',4,400,'CO87','SL41','B005' );
INSERT INTO propertyForRent VALUES('PG4','6 Lawrence St','Glasgow','G11 9QX','Flat',3,350,'CO40', NULL, 'B003');
INSERT INTO propertyForRent VALUES('PG36','2 Manor Rd','Glasgow','G32 4QX','Flat',3,375,'CO93','SG37','B003' );
INSERT INTO propertyForRent VALUES('PG21','18 Dale Rd','Glasgow','G12','House',5,600,'CO87','SG37','B003');
INSERT INTO propertyForRent VALUES('PG16','5 Novar Dr','Glasgow','G12 9AX','Flat',4,450,'CO93','SG37','B003' );

-- registration for the clients who want to rent out house
CREATE TABLE clientregistration
(
 clientNo char(5) PRIMARY KEY,
 fName varchar(20),
 branchNo char(5),
 baddress varchar(50),
 regBy char(5),
 regDate date,
 type char(10),
 maxRent int,
 foreign key(branchNo) references branch(branchNo),
 foreign key(regBy) references staff(staffNo)
);

INSERT INTO clientregistration values ('CR76','Elena','B003','163 Main St, Glasgow','SA9','2015-01-23','Flat',700);
INSERT INTO clientregistration values ('CR56','Edward','B005','22 Deer Rd, London','SL21','2014-04-13','House',850);
INSERT INTO clientregistration values ('CR74','Nathan','B003','163 Main St, Glasgow','SA9','2013-11-16','Flat',600);
INSERT INTO clientregistration values ('CR62','Ariana','B007','16 Argyll St, Aberdeen','SL21','2014-03-07','House',1600);
INSERT INTO clientregistration values ('CR54','Belinda','B002','56 Clover Dr, London','SG37','2013-06-13','House',900);

-- details of properties viewed by clients
CREATE TABLE  viewing
(clientNo char(5) not null,
 propertyNo char(5) not null,
 viewDate date,
 comment varchar(70),
 foreign key(clientNo) references clientregistration(clientNo),
 foreign key(propertyNo) references propertyforrent(propertyNo)
);

INSERT INTO viewing VALUES('CR56','PA14','2015-05-24','too small');
INSERT INTO viewing VALUES('CR76','PG4','2015-04-20','too remote');
INSERT INTO viewing VALUES('CR56','PG4','2015-05-26','');
INSERT INTO viewing VALUES('CR62','PA14','2015-05-14','no dining room');
INSERT INTO viewing VALUES('CR56','PG36','2015-04-28','');

SET FOREIGN_KEY_CHECKS=0;
-- Houses that are rented out
create table lease
(
leaseId int primary key,
clientNo char(5),
Rent int not null,
Deposit Boolean,
paymentMethod varchar(30),
propertyNo char(5),
rentStartDt varchar(20),
rentEndDt varchar(20),
DurationInYears float,
FOREIGN KEY (propertyNo) references propertyforrent(propertyNo),
foreign key(clientNo) references clientregistration(clientNo)
);

insert into lease values (1,'CR56',450,TRUE,'cash','PG36','01/06/2004','31/05/2005',1);
insert into lease values (2,'CR74',1800,TRUE,'cheque','PL94','01/03/2003','31/04/2006',3);

SELECT propertyNo,city,type,rent FROM propertyForRent WHERE propertyNo not in (select propertyNo from lease);

show tables;
select * from branch;
select * from staff;
select * from privateowner;
select * from propertyforrent;
select * from clientregistration;
select * from viewing;
select * from lease;

delete from viewing where propertyNo = 'PL08';
delete from lease where leaseId = 3;

desc branch;
desc staff;
desc privateowner;
desc propertyforrent;
desc clientregistration;
desc lease;
desc viewing;

-- Queries required by the Branch:
 -- a) 
select * from branch where city = 'London';

-- b)
select  count(branchNo) from branch where city = 'Glasgow';

-- c)
select * from staff  order by branchNo;

-- d)
select count(staffNo),sum(salary) as total from staff;

-- e)
select count(staffNo),position 
from staff ,branch 
where staff.branchNo=branch.branchNo and  city='Glasgow' group by position;

-- f)
select branchNo,staffNo,fName,Sex,telephone 
from staff 
where position ='Manager' order by branchNo;

-- g)
select staffNo,fName,Sex,telephone 
from staff,branch 
where staff.branchNo=branch.branchNo and position ='Supervisor' order by city;

-- h)
select propertyNo , street,city , type , rent
from propertyforrent
where city = 'Glasgow'
order by rent;

-- i)
select * from propertyforRent 
where StaffNo is not null;

-- j)
select count(s.propertyNo),s.staffNo
from propertyforrent as s,propertyforrent as t
where (s.staffNo,s.propertyNo)=(t.staffNo,t.propertyNo) and s.staffNo is not null
group by s.staffNo;

-- k)
select propertyforrent.ownerNo,propertyNo,type,rooms,rent,street,city,postcode,fname,branchNo
from propertyforrent ,privateowner
where propertyforrent.ownerNo=privateowner.ownerNo
order by branchNo;

-- l)
select count(propertyNo),type 
from propertyforrent group by type;

-- m)
   -- (wrong) select * from privateOwner,propertyforRent where privateOwner.OwnerNo=propertyforRent.OwnerNo and count(propertyNo)>1;   syntax wrong count inside where 

select * from privateowner 
where ownerNo in (
select ownerNo 
from propertyforrent
group by ownerNo  
having count(*)>1);


-- n)
select * 
from propertyforRent 
where type='flat' and rent<500 and rooms =3 and city ='Aberdeen';

select *
from propertyforrent
where type='Flat' and propertyNo in (select propertyNo
									 from propertyforrent
                                     where rent<500 and city='Aberdeen' and rooms>=3);


-- o)
select ClientRegistration.branchNo,ClientNo,fName,type,MaxRent 
from ClientRegistration,Branch 
where ClientRegistration.branchNo=Branch.branchNo;

-- p)

SELECT leaseId
FROM lease
WHERE lease.rentEndDt BETWEEN now() AND date_add(now(),interval 1 month);

-- q)
SELECT leaseId
FROM lease l
WHERE l.rentEndDt BETWEEN now() AND date_add(now(),interval 1 month);

-- r)
select count(leaseID) 
from lease where DurationInYears < 1 and 
propertyNo in (select propertyNo from propertyforRent where city ='london');

-- 2nd queries list 

-- a

SELECT staff.staffNo, staff.fName, staff.position, staff.sex, staff.telephone, staff.DOB, staff.salary, staff.branchNo
FROM staff
INNER JOIN branch ON staff.branchNo = branch.branchNo
where staff.position = 'Assistant';

-- b 
select fName 
from staff 
where position = 'Assistant'
-- group by branchNo 
order by fName ASC;

-- c  // deposit ledu ??
select p.propertyNo , p.ownerNo ,p.branchNo			
from propertyforrent p,privateowner o;


-- d
select p.propertyNo ,p.staffNo,p.branchNo
from propertyforrent p,staff s
where p.staffNo = s.staffNo;

-- e // staff names clientreg lo names diff

select r.clientNo , s.fName,s.barnchNo
from clientregistrartion r , staff s
where r.fName = s.fName;


-- f
select * from propertyforrent
where city = 'Glasgow' and rent < 450;

-- g

select DISTINCT r.ownerNo , p.fName, p.telNo
from privateowner p ,propertyforrent r
where p.ownerNo = r.ownerNo;

-- h
select comment , clientNo
from viewing ;

-- i 
select v.comment, v.clientNo , c.fName
from viewing v , clientregistration c
where v.comment is NULL;

-- j

select l.clientNo, p.propertyNo
from lease l , propertyforrent p
where l.propertyNo = p.propertyNo;

-- k

select * from lease 
where rentEndDt like '31_0_2023';

-- l  /// rented out di data ledu

select *
from propertyforrent p ,clientregistration c;


-- m  // prefernce ledu changes cheyyali

select distinct p.branchNo , p.type,p.rent , c.clientNo
from propertyforrent p,clientregistration c
where p.type = c.type and p.rent<c.maxRent and p.branchNo = c.branchNo;

delete from staff where staffNo = 'SL44';
delete from clientregistration where clientNo = 'CR41';
delete from privateowner where ownerNo = 'CO61';
delete from propertyforrent where propertyNo = 'PL08';
