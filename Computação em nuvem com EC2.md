# Computação em Nuvem com EC2



### Bootcamp desafio:
Montar um fluxo de arquitetura AWS mostrando os conceitos aprendidos ao longo do bloco de conhecimento


**ATIVIDADE**

**Caso:** Um cliente pode realizar solicitação para emissão de documentos para uma plataforma.

**Fluxo:** 

O cliente acessaria a plataforma que está hospedada em uma máquina virtual (Instância EC2) solicitando a emissão de um determinado documento.
Arquivos são armazenados e consultados em S3, por conta disso, o fluxo encaminha ao S3, que gera uma chamada ao Lambda assim que identifica uma solicitação de um novo documento.
O lambda trabalha e consegue gerar os arquivo, devolvendo ao S3 que hospeda.
Estando no S3 o documento pode ser disponibilizado na plataforma e o cliente pode retornar o acesso a plataforma obtendo seu arquivo.
Para cuidar de eventuais perdas, um backup é realizado periodicamente em cima do EBS a fim de não perder dados importantes de pontos do sistema.


![Fluxo AWS](Imagens/AWS%20Fluxo.drawio.png)
