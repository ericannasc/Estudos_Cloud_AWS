# Computação em Nuvem com EC2

### APRENDIZADOS (Até o momento)

A AWS possui diversos serviços em nuvem que podem ser categorizados em:
- **IaaS:** Infraestrutura como serviço
- **PaaS:** Plataforma como serviço
- **SaaS:** Software como serviço

#### Regiões e Zonas de disponibilidade
A cobertura da AWS é distribuido no que chamamos de Regions, possuindo diversos pontos espalhados pelo mundo. Cada Region é composta por 2 ou 3 zonas de disponibilidades que são datacenters isolados.

As regions podem oferecer serviços diferentes umas das outras, assim como varior o valor cobrado por um determinado serviço. Embora uma região possa ser mais barata, na hora de planejar uma arquitetura deve ser considerado a latência que os principais clientes que acessam a plataforma/serviço teriam, pois quanto mais distante, maior seria a latência.

Embora haja esse problema, é possível com AWS gerir formas de ter pontos de cache em diferentes regiões (útil caso o produto seja acessado de diversos locais do mundo). Nesse caso, haveriam cópias carregadas em regiões mais próxima ao cliente após um primeiro ter acessado (esse primeiro a acessar receberia lentidão, e demais a acessarem teria maior velocidade).

#### Amazon EC2
São máquinas virtuais que AWS disponibiliza para que seja possível a execução de um projeto sem a necessidade de montar uma infraestrutura física previamente. Sua vantagem é a praticidade com o aluguel de máquinas na nuvem sem precisar investir em espaço, equipamentos, energia, atualizações, entre outros pontos que geram mais gastos com tempo e financeiro.

Instâncias EC2 possuem diferentes famílias que diz respeito a capacidade do Hardware que pode ser alugado. Um bom gestor, deve escolher a familia com base no que a aplicação de fato necessita em recurso para não haver gastos excessivos ou má desempenho.

#### Amazon EBS
Funcionam como HDs externos que podem ser adicionados a instância EC2, que por si só, vem com a configuração e o Sistema Operacional escolhido na hora de sua configuração. Adicionando um EBS é possível particionar o armazenamento para organização dos tipos de dados.

#### Snapshot EBS
O snapshot é o backup realizado do EBS, capturando de forma incremental o volume EBS para que não sejam perdidos caso ocorra um eventual problema. Por meio de Snapshot também é possível transitar de uma Region para outra.

#### Amazon S3
É um serviço de armazenamento de arquivos que AWS oferece, sendo possível configurar ciclo de vida para os arquivos a depender do tempo em que ficam hospedados. Além disso, a S3 também possui classes de armazenamento, sendo Standard utilizada para arquivos com frequente acesso, e Glacier para arquivos com mais dificil acesso, onde neste, teria que abrir uma solicitação para que seja recuperado. O cliclo de vida pode ser definido por tempo em que um arquivo não é acessado, por exemplo, passado 90 dias sem interação, automaticamente ele passa para o Glacier.

#### Amazon AMI
É uma cópia que pode ser feita de instâncias EC2 quando deseja-se outras máquinas virtuais com mesma configuração. O intuito é facilitar a criação de outras máquinas ao invés de criar uma a uma.

---


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
