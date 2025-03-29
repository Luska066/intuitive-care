CREATE TABLE OPERADORAS(
    id int primary key auto_increment not null,
    DATA varchar(255),
    REG_ANS varchar(255),
    CD_CONTA_CONTABIL varchar(1000),
    VL_SALDO_INICIAL float,
    VL_SALDO_FINAL float
);