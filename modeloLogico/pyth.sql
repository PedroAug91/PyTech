-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema pytech
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema pytech
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `pytech` DEFAULT CHARACTER SET utf8 ;
USE `pytech` ;

-- -----------------------------------------------------
-- Table `pytech`.`produto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pytech`.`produto` (
  `idproduto` INT NOT NULL AUTO_INCREMENT,
  `NomeProduto` VARCHAR(45) NOT NULL,
  `Preco` VARCHAR(45) NOT NULL,
  `Descricao` VARCHAR(1000) NOT NULL,
  PRIMARY KEY (`idproduto`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pytech`.`fornecedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pytech`.`fornecedor` (
  `idfornecedor` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  `Email` VARCHAR(45) NOT NULL,
  `CNPJ` VARCHAR(45) NOT NULL,
  `Senha` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idfornecedor`),
  UNIQUE INDEX `Email_UNIQUE` (`Email` ASC) VISIBLE,
  UNIQUE INDEX `CNPJ_UNIQUE` (`CNPJ` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pytech`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pytech`.`cliente` (
  `idCliente` INT NOT NULL AUTO_INCREMENT,
  `CPF` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `senha` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCliente`),
  UNIQUE INDEX `Clientecol_UNIQUE` (`CPF` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pytech`.`telefone`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pytech`.`telefone` (
  `idtelefone` INT NOT NULL AUTO_INCREMENT,
  `Cliente_idCliente` INT NULL,
  `fornecedor_idfornecedor` INT NULL,
  PRIMARY KEY (`idtelefone`),
  INDEX `fk_telefone_Cliente_idx` (`Cliente_idCliente` ASC) VISIBLE,
  INDEX `fk_telefone_fornecedor1_idx` (`fornecedor_idfornecedor` ASC) VISIBLE,
  CONSTRAINT `fk_telefone_Cliente`
    FOREIGN KEY (`Cliente_idCliente`)
    REFERENCES `pytech`.`cliente` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_telefone_fornecedor1`
    FOREIGN KEY (`fornecedor_idfornecedor`)
    REFERENCES `pytech`.`fornecedor` (`idfornecedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pytech`.`endereco`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pytech`.`endereco` (
  `idEndereco` INT NOT NULL AUTO_INCREMENT,
  `cidade` VARCHAR(45) NOT NULL,
  `bairro` VARCHAR(45) NOT NULL,
  `estado` VARCHAR(45) NOT NULL,
  `rua` VARCHAR(45) NOT NULL,
  `NumCasa` INT NOT NULL,
  `Cliente_idCliente` INT NULL,
  `fornecedor_idfornecedor` INT NULL,
  PRIMARY KEY (`idEndereco`),
  INDEX `fk_Endereco_Cliente1_idx` (`Cliente_idCliente` ASC) VISIBLE,
  INDEX `fk_Endereco_fornecedor1_idx` (`fornecedor_idfornecedor` ASC) VISIBLE,
  CONSTRAINT `fk_Endereco_Cliente1`
    FOREIGN KEY (`Cliente_idCliente`)
    REFERENCES `pytech`.`cliente` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Endereco_fornecedor1`
    FOREIGN KEY (`fornecedor_idfornecedor`)
    REFERENCES `pytech`.`fornecedor` (`idfornecedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pytech`.`carrinho`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pytech`.`carrinho` (
  `idcarrinho` INT NOT NULL AUTO_INCREMENT,
  `Cliente_idCliente` INT NOT NULL,
  PRIMARY KEY (`idcarrinho`),
  INDEX `fk_carrinho_Cliente1_idx` (`Cliente_idCliente` ASC) VISIBLE,
  CONSTRAINT `fk_carrinho_Cliente1`
    FOREIGN KEY (`Cliente_idCliente`)
    REFERENCES `pytech`.`cliente` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pytech`.`venda`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pytech`.`venda` (
  `idvenda` INT NOT NULL AUTO_INCREMENT,
  `dataCompra` VARCHAR(45) NOT NULL,
  `carrinho_idcarrinho` INT NOT NULL,
  PRIMARY KEY (`idvenda`),
  INDEX `fk_venda_carrinho1_idx` (`carrinho_idcarrinho` ASC) VISIBLE,
  CONSTRAINT `fk_venda_carrinho1`
    FOREIGN KEY (`carrinho_idcarrinho`)
    REFERENCES `pytech`.`carrinho` (`idcarrinho`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pytech`.`carrinho_has_produto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pytech`.`carrinho_has_produto` (
  `idcarrinho_has_produto` INT NOT NULL,
  `carrinho_idcarrinho` INT NOT NULL,
  `produto_idproduto` INT NOT NULL,
  `QTD` INT NOT NULL,
  `Total` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idcarrinho_has_produto`, `carrinho_idcarrinho`, `produto_idproduto`),
  INDEX `fk_carrinho_has_produto_carrinho1_idx` (`carrinho_idcarrinho` ASC) VISIBLE,
  INDEX `fk_carrinho_has_produto_produto1_idx` (`produto_idproduto` ASC) VISIBLE,
  CONSTRAINT `fk_carrinho_has_produto_carrinho1`
    FOREIGN KEY (`carrinho_idcarrinho`)
    REFERENCES `pytech`.`carrinho` (`idcarrinho`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_carrinho_has_produto_produto1`
    FOREIGN KEY (`produto_idproduto`)
    REFERENCES `pytech`.`produto` (`idproduto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pytech`.`imagemProduto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pytech`.`imagemProduto` (
  `idImagemProduto` INT NOT NULL AUTO_INCREMENT,
  `Caminho` VARCHAR(1000) NOT NULL,
  `Imagem_idImagem` INT NOT NULL,
  `produto_idproduto` INT NOT NULL,
  PRIMARY KEY (`idImagemProduto`),
  INDEX `fk_ImagemProduto_produto1_idx` (`produto_idproduto` ASC) VISIBLE,
  CONSTRAINT `fk_ImagemProduto_produto1`
    FOREIGN KEY (`produto_idproduto`)
    REFERENCES `pytech`.`produto` (`idproduto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pytech`.`estoque`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pytech`.`estoque` (
  `idestoque` INT NOT NULL AUTO_INCREMENT,
  `quantidade produto` VARCHAR(45) NOT NULL,
  `fornecedor_idfornecedor` INT NOT NULL,
  `produto_idproduto` INT NOT NULL,
  PRIMARY KEY (`idestoque`),
  INDEX `fk_estoque_fornecedor1_idx` (`fornecedor_idfornecedor` ASC) VISIBLE,
  INDEX `fk_estoque_produto1_idx` (`produto_idproduto` ASC) VISIBLE,
  CONSTRAINT `fk_estoque_fornecedor1`
    FOREIGN KEY (`fornecedor_idfornecedor`)
    REFERENCES `pytech`.`fornecedor` (`idfornecedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_estoque_produto1`
    FOREIGN KEY (`produto_idproduto`)
    REFERENCES `pytech`.`produto` (`idproduto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pytech`.`categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pytech`.`categoria` (
  `idcategoria` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `descricao` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idcategoria`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pytech`.`categoriaProduto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pytech`.`categoriaProduto` (
  `idcategoriaProduto` INT NOT NULL AUTO_INCREMENT,
  `produto_idproduto` INT NOT NULL,
  `categoria_idcategoria` INT NOT NULL,
  PRIMARY KEY (`idcategoriaProduto`),
  INDEX `fk_categoriaProduto_produto1_idx` (`produto_idproduto` ASC) VISIBLE,
  INDEX `fk_categoriaProduto_categoria1_idx` (`categoria_idcategoria` ASC) VISIBLE,
  CONSTRAINT `fk_categoriaProduto_produto1`
    FOREIGN KEY (`produto_idproduto`)
    REFERENCES `pytech`.`produto` (`idproduto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_categoriaProduto_categoria1`
    FOREIGN KEY (`categoria_idcategoria`)
    REFERENCES `pytech`.`categoria` (`idcategoria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
