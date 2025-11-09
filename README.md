# mlflow-huggingface-integration
Escrever
Resumo

Os projetos do MLflow são um formato para empacotar o código de ciência de dados para executá-lo de forma reproduzível e reutilizável. Eles consistem em código, suas dependências e metadados.

Os projetos podem especificar detalhes como nome, ambientes, parâmetros e pontos de entrada em um arquivo MLproject. Caso contrário, as convenções são usadas para inferir esses detalhes. 

Os projetos podem ser executados local ou remotamente usando o mlflow run. Parâmetros, argumentos e sinalizadores adicionais podem configurar as execuções.

Os projetos do MLflow facilitam a iteração rápida. Eles também permitem a construção de fluxos de trabalho de várias etapas chamando mlflow.projects.run() em um programa.

Os casos de uso incluem modularização de código, ajuste de hiperparâmetro, validação cruzada e empacotamento de código existente.

Perguntas para reflexão

Qual é a diferença entre os projetos do MLflow e o simples controle de versão e compartilhamento de código? Que valor adicional eles oferecem?

Que tipos de desafios podem surgir ao tentar dividir um pipeline de aprendizado de máquina em etapas reutilizáveis separadas? Como o MLflow pode ajudar a resolver alguns deles?

Quais são alguns exemplos de fluxos de trabalho ou casos de uso que se beneficiariam da implementação como projetos do MLflow?

Qual seria a viabilidade de converter uma base de código de aprendizado de máquina existente em um projeto do MLflow? O que estaria envolvido?

Exercícios de desafio

Pegue um script de aprendizado de máquina existente e configure-o como um projeto MLflow com conda.yaml, arquivo MLproject etc.

Crie um fluxo de trabalho de duas etapas usando o MLflow Projects para dividir os dados e, em seguida, treinar e avaliar um modelo.

Use o MLflow Projects para iniciar vários trabalhos de ajuste de hiperparâmetros distribuídos, acompanhando os resultados.

