CREATE DATABASE charging_station_v2;

USE charging_station_v2;

#用户表
CREATE TABLE USER(
	uid INT PRIMARY KEY AUTO_INCREMENT, #主键id
	user_name VARCHAR(20) NOT NULL UNIQUE, #用户名
	PASSWORD VARCHAR(20) NOT NULL, #密码
	NAME VARCHAR(20) NOT NULL, #真实姓名
	telephone VARCHAR(20) NOT NULL, #电话
	department VARCHAR(10) NOT NULL, #所属部门
	user_grade INT NOT NULL, #用户等级 0代表普通用户，1代表管理员
	check_status INT NOT NULL #0代表未审核（注册的时候），1代表管理员审核通过（只有这个标记位为1的时候才能登录进去）
)ENGINE=INNODB DEFAULT CHARSET=utf8;

#充电站包含数据
CREATE TABLE table_charge_station(
	sid INT PRIMARY KEY AUTO_INCREMENT,
	#s_flag INT DEFAULT 0, #用于在数据展示页面中加载出的充电站名是全部数据都加载进数据库当中的
	station_name VARCHAR(20) NOT NULL, #充电站名(加索引)，项目中根据充电站名称查找该充电站的所有充电桩数据
	station_addr VARCHAR(50) NOT NULL, #充电站地址
	longitude DECIMAL(10, 6) NOT NULL, #充电站经度
	latitude DECIMAL(10, 6) NOT NULL, #充电站纬度
	s_num INT DEFAULT 0, #用于展示该充电站中的充电桩数量
	s_local VARCHAR(20) NOT NULL, #充电站所在区县
	s_jiaoliu_num INT DEFAULT 0, #该充电站中交流充电桩的数量
	s_zhiliu_num INT DEFAULT 0, #该充电站中直流充电桩的数量
	start_time TIMESTAMP NOT NULL DEFAULT 0, #时间戳类型，记录起始时间 '0000-00-00 00:00:00' 这个可以用来查重！！！
	INDEX idx_name (station_name) #建立辅助索引
)ENGINE=INNODB DEFAULT CHARSET=utf8;

#充电站在某时段的数据表
CREATE TABLE table_station_period(
	sid INT, #与充电站表sid一直
	start_time TIMESTAMP NOT NULL DEFAULT 0, #时间戳类型，记录起始时间 '0000-00-00 00:00:00'
	end_time TIMESTAMP NOT NULL DEFAULT 0, #时间戳类型，记录终止时间，end_time - start_time = 时间段
	env_temper DECIMAL(4, 2) NOT NULL, #环境温度
	env_shidu DECIMAL(4, 2) NOT NULL, #相对湿度
	loss_energy DECIMAL(8, 3), #充电桩损耗数据
	total_energy DECIMAL(8, 3)#充电站所有充电桩不同时间段的总电能数据
)ENGINE=INNODB DEFAULT CHARSET=utf8;

#保存静态数据,充电桩信息，不根据时间段的变化而变化
CREATE TABLE table_charge_pile(
	pid INT ,#充电站中的每个充电桩id，（sid，pid）需要建立联合索引
	sid INT NOT NULL, #所属充电站
	#pid INT NOT NULL, #充电站中的每个充电桩id，（sid，pid）需要建立联合索引
	model_type VARCHAR(20) NOT NULL, #型号，EV-DC-02
	factory_num VARCHAR(20) NOT NULL, #出厂编号，020200323001
	nomial_level INT NOT NULL, #标称等级
	install_time_span BIGINT NOT NULL, #充电桩安装时长
	carrieroperator VARCHAR(20) NOT NULL, #运营商
	manufacturer VARCHAR(20) NOT NULL, #生产厂家
	#maintain_freq INT NOT NULL, #运营商维护频次
	Measurement_error DECIMAL(5, 2), #充电桩n的计量误差，在不同时段的计量误差是一样的，根据所给矩阵公式可求出
	risk_level INT, #如果有计算过，记为0-3四个等级（低、较低、较高、高），业务层需判断，如果在某些时间段计算过，就直接取
	start_time TIMESTAMP NOT NULL DEFAULT 0, #时间戳类型，记录起始时间 '0000-00-00 00:00:00' 这个可以用来查重！！！
	KEY idx_sid_pid (sid, pid) #为所属充电站与充电桩建立联合索引关系
)ENGINE=INNODB DEFAULT CHARSET=utf8;

#保存动态数据,充电桩信息，根据时间段的变化而变化
CREATE TABLE table_pile_period(
	sid INT NULL, #所属充电站的序号
	pid INT NULL, #所属充电桩的序号
	start_time TIMESTAMP NOT NULL DEFAULT 0, #时间戳类型，记录起始时间 '0000-00-00 00:00:00'
	end_time TIMESTAMP NOT NULL DEFAULT 0, #时间戳类型，记录终止时间，end_time - start_time = 时间段
	use_freq DECIMAL(8, 2) NOT NULL, #使用频率
	energy DECIMAL(8, 3), #充电桩n在时段t的电能计量数据
	KEY idx_sid_pid (sid, pid) #为所属充电站与充电桩建立联合索引关系
)ENGINE=INNODB DEFAULT CHARSET=utf8;