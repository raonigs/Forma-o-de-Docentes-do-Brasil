# Formação de Docentes do Brasil
Análise dos dados do INEP sobre as formações de docentes do Brasil. Os dados foram obtidos pelo datalake do repositório da @basedosdados, uma limpeza e pré-processamento foram feitos em linguagem SQL para extração dos dados primários e posterior análise exploratória, visualização, criação de gráficos e elaboração do Dashboard.

O primeiro gráfico (barras empilhadas) mostra as categorias de professores e suas porcentagens nas diferentes categorias de ensino (Educação Infantil, EJA Ensino Fundamental, EJA Ensino Médio, Ensino Fundamental e Ensino Médio) para o ano de 2020:

![fig](https://github.com/raonigs/Forma-o-de-Docentes-do-Brasil/assets/98754863/5912a80b-9bfc-4d00-979b-cf2826c386a6)

O segundo gráfico (linha de série temporal) mostra as categorias de professores e suas porcentagens ao longo dos anos (2013 à 2020):

![fig1](https://github.com/raonigs/Forma-o-de-Docentes-do-Brasil/assets/98754863/1e79ec4c-e425-47ef-8545-a574d3386ca2)


O terceiro gráfico (barras empilhadas) mostra as categorias de professores e suas porcentagens nos diferentes estados no ano de 2020:

![fig2](https://github.com/raonigs/Forma-o-de-Docentes-do-Brasil/assets/98754863/d389378c-c10e-4175-9980-793abedd3d06)


O quarto gráfico (pie chart) mostra as categorias de professores nas diferentes redes de ensino (municipal, estadual, federal, público e privado) para o ano de 2020:

![fig3](https://github.com/raonigs/Forma-o-de-Docentes-do-Brasil/assets/98754863/3e4690a8-b313-49dd-bc5c-ced01a11c3d5)


Logo após, foi utilizado a biblioteca Dash para elaboração do Dashboard com todos os gráficos feitos (algumas alterações estéticas foram feitas nos gráficos para adaptação ao layoute e paletas de cores escolhidas):

![dashboard](https://github.com/raonigs/Forma-o-de-Docentes-do-Brasil/assets/98754863/e3fcb432-d6c2-41ca-bdd0-58f44671dcea)




