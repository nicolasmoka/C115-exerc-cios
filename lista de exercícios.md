## 1. Explique o conceito de Web Service segundo a definição da Gartner.

Especificamente, um Web Service é um componente de software que pode ser acessado por outra aplicação (como um cliente, um servidor ou outro Web Service) por meio do uso de  protocolos e transportes ubíquos e altamente disponíveis, como o Hipertext Transport Protocol (HTTP). Esforços conjuntos entre a IBM e a Microsoft, com o apoio de outros fornecedores, como a Ariba e a Iona Technologies, resultaram em um acordo sobre um conjunto básico de padrões baseados em XML para definição, descoberta e chamada remota de interfaces de serviços web. Eles incluem:
- Web Services Description Language (WSDL) para descrever interfaces de serviços web
- Universal Description, Discovery and Integration (UDDI) como meio para os usuários publicarem e localizarem serviços web disponíveis, suas características e interfaces
- Simple Object Access Protocol (SOAP), que permite que um aplicativo chame um serviço web 

## 2. Explique a função do protocolo SOAP e descreva a composição de seu envelope.

Projetado para ser simples, o SOAP cria um mapeamento transparente das definições da Interface Definition Language (IDL) do Distributed Component Object Model (DCOM) e da Extensible Markup Language (XML). Ele fornece a tecnologia-chave para o transporte na Internet de próxima geração como um conjunto de serviços eletrônicos.
O envelope SOAP é composto pelo SOAP header, que é utilizado para a passagem de mensagens de controle e pelo SOAP body, que contém os dados a serem transmitidos.

## 3. Quais são os três elementos principais de uma arquitetura de Web Service?

Registro de serviço, fornecedor de serviços e Solicitante de serviços.

## 4. O que é WSDL e quais são os elementos básicos que o compõem?

WSDL e uma descricao em formato XML de um Web Service que utilizara SOAP como protocolo.

Seus elementos básicos são:
- \<types>: para descrever os tipos de dados suportados pelo serviço em questão;
- \<message>: para especificar os padrões de entrada e saída de dados dos web services;
- \<portType>: para descrever os agrupamentos lógicos das operações. São as operações executadas pelo web service;
- \<binding>: para especificar os protocolos de comunicação que os web services utilizam;
- \<operation>: região que permite a especificação das assinaturas dos métodos disponibilizados;
- \<definitions>: elemento padrao de todos os documentos WSDL. Permite efetuar descricoes sobre schemas e namespaces e sobre o proprio documento WSDL.

## 5. Qual é a função do UDDI em Web Services?

O UDDI permite que pessoas e empresas registrem e publiquem seus web services, tornando-os acessíveis a outros sistemas. ELe também facilita a localização de serviços disponíveis na rede, inclusive novos serviços, com a mesma facilidade que os antigos. Por fim, ele ajuda  aplicações a entenderem como interagir com um serviço, fornecendo informações sobre sua interface e semântica.

## 6. O que é REST e quem o criou?

Criado por Roy Fielding em 2000, como tese de doutorado (PHD) na UC Irvine, Respresentational State Transfer (REST) é um conjunto de regras que permitem a criação de um projeto com interfaces bem definidas.

## 7. Qual é a função de um recurso (Resource) no REST e como ele é identificado? 

Um recurso é a chave da abstração no REST. Ele é qualquer coisa importante o sufuciente para ser referenciado com um URI (Uniform Resourse Identifier).

## 8. O que é virtualização e quais são seus principais tipos de recursos virtualizados?

A virtualização é o processo de criar uma representação virtual via software de recursos físicos, permitindo que múltiplos ambientes independentes compartilhem o mesmo hardware. Ela é amplamente usada para otimizar o uso de servidores, melhorar a segurança, facilitar testes e reduzir custos operacionais.

Alguns recursos virtualizados incluem:
- Servidores: Permite executar múltiplos sistemas operacionais em um único servidor físico.
- Armazenamento: Cria volumes de armazenamento virtualizados, independentes do hardware físico.
- Redes: Separa recursos de rede do hardware físico, criando redes virtuais (ex: VLAN, SDN, NFV).
- Desktops: Executa ambientes de trabalho remotamente, via infraestrutura de desktop virtual (VDI).
- Aplicações: Permite que aplicativos sejam executados em ambientes isolados, como containers.

## 9. O que é um container Docker e o que ele empacota?

Um container Docker é uma unidade padronizada de software que empacota tudo o que uma aplicação precisa para funcionar de forma consistente em qualquer ambiente, seja no computador do desenvolvedor, em servidores ou na nuvem.

Um contaier Docker inclui o código da aplicação, bibliotecas e dependências, ferramentas do sistema e configurações necessárias. Tudo isso é reunido em uma imagem Docker, que funciona como um snapshot do ambiente ideal para rodar a aplicação.