
/* GRUPOS DE COMNADOS DO SQL
1 DDL - DATA DEFINITION LANGUAGE
  CREATE (cria objetos no banco de dados)
  ALTER (modifica um objeto existente no BD)
  DROP  (exclui uma tabela ou outra coisa na BD)

2 DML - DATA MANIPULATION LANGUAGE
  INSERT(cria um registro 'linha')
  UPDATE(atualiza ou modifica registros no BD)
  DELETE( exclui registros no BD)

3 DCL - DATA CONTROL LANGUAGE
  GRANT(dá privilégios a um usuário)
  REVOKE(retira os privilégios fornecidos ao usuário)

4 DQL - DATA QUERRY LANGUAGE
  SELECT (obtem registros de uma ou mais tabelas)

COMPOSIÇÃO DE UM BD
 * TABELAS (são os dados em um banco, são separados por campos e linhas)
 * CAMPOS (COLUNAS) - são colunas das tabelas (vertical)
 * REGISTROS (LINHAS - tuplas) - são as entradas inviduais nas tabelas (horizontal)
 


aprendendo FROM:
SELECT
 -- SQL Server, Postgres, Oracle, MySql

 SELCT coluna1, coluna2
 FROM tabela

 SELECT *
 FROM

aprendendo DISTINCT:

SELECT DISTINCT
FROM person.person

aprendendo WHERE:

SELECT coluna1, coluna2, coluna_n
FROM tabela
WHERE condição

/*

OPREADOR  -   DESCRIÇÃO
=             IGUAL
>             MAIOR QUE
<             MENOR QUE
>=            MAIOR OU IGUAL QUE
<=            MENOR OU IGUAL QUE
<>            DIFERENTE DE
AND           OPRADOR LOGICO "E"
OR            OPERADOR LOGICO "OU"

*/

aprendendo COUNT:

SELECT COUNT (*)
FROM person.person