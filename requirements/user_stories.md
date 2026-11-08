# 👥 Histórias de Usuário (User Stories) - Rede Delas

Este documento detalha as necessidades das usuárias e os critérios de aceite que orientaram o desenho das telas do protótipo Rede Delas. A coluna RF relaciona cada história ao requisito funcional correspondente (RF.md).

## 1. Infraestrutura e Acesso (Core)

| ID | Persona | História de Usuário | Critério de Aceite | RF |
| :--- | :--- | :--- | :--- | :--- |
| **US01** | Visitante | Como estudante da UTFPR, desejo me cadastrar no app usando meu e-mail institucional, para garantir que a rede seja exclusiva para a comunidade acadêmica. | Validação do domínio `@alunos.utfpr.edu.br` no formulário de cadastro. | RF01 |
| **US02** | Usuária | Como usuária cadastrada, desejo realizar login com senha ou recuperar meu acesso via e-mail, para proteger meus dados e conexões. | Tela de login e fluxo "Esqueci minha senha" com feedback de envio. | RF02 |
| **US03** | Usuária | Como usuária, desejo configurar meu perfil (foto, curso, período, interesses e biografia), para que outras alunas me identifiquem na rede. | Cadastro em duas etapas e edição de perfil, com campo para adicionar foto. | RF03 |
| **US04** | Usuária | Como aluna avançada, desejo sinalizar minha disponibilidade como mentora, para que calouras possam me encontrar para tirar dúvidas. | Chave "Desejo ser mentora" no cadastro e na edição do perfil. | RF04 |
| **US19** | Usuária | Como usuária, desejo ver ao abrir o app um resumo com a inspiradora do dia, a mentoria, os eventos e o fórum, para facilitar minha navegação. | Tela inicial com destaques e acesso aos quatro módulos. | RF05 |

## 2. Módulo: Elas Inspiram (Role Models)

| ID | Persona | História de Usuário | Critério de Aceite | RF |
| :--- | :--- | :--- | :--- | :--- |
| **US05** | Usuária | Como usuária, desejo navegar por uma galeria de perfis inspiradores, para conhecer a trajetória de mulheres de sucesso em STEM. | Grade com foto, nome, área e categoria, com busca e filtros. | RF06 |
| **US06** | Usuária | Como usuária, desejo salvar perfis inspiradores como favoritos, para acessá-los rapidamente em momentos de desmotivação. | Ícone de estrela que adiciona ou remove o perfil da aba "Favoritas". | RF07 |

## 3. Módulo: Conexões (Mentoria entre pares)

| ID | Persona | História de Usuário | Critério de Aceite | RF |
| :--- | :--- | :--- | :--- | :--- |
| **US07** | Mentoranda | Como aluna, desejo filtrar mentoras por disciplinas específicas (ex.: Cálculo I), para encontrar ajuda técnica pontual. | Campo de busca e filtros por disciplina na lista de mentoras. | RF08 |
| **US08** | Mentoranda | Como aluna, desejo enviar uma solicitação de mentoria descrevendo minha dúvida e acompanhar o pedido, para iniciar uma conversa com uma veterana. | Botão "Solicitar Mentoria" que abre um modal de mensagem; pedido acompanhado por status e passível de cancelamento. | RF09 |
| **US09** | Mentora | Como mentora, desejo visualizar a dúvida e o perfil da solicitante antes de aceitar ou recusar, e encerrar a mentoria quando concluída, para gerenciar minha disponibilidade. | Painel "Minhas Mentorias" (pendentes, em andamento e concluídas), com recusa confirmada e opção de finalizar. | RF10 |
| **US10** | Mentoranda | Como mentoranda, desejo avaliar a experiência de mentoria ao finalizá-la, para contribuir com a melhoria da rede. | Modal de finalização com escala de 5 estrelas e campo de comentário. | RF10 |

## 4. Módulo: Comunidade (Agenda Acadêmica)

| ID | Persona | História de Usuário | Critério de Aceite | RF |
| :--- | :--- | :--- | :--- | :--- |
| **US11** | Usuária | Como usuária, desejo visualizar uma agenda centralizada de eventos (palestras, workshops), para me manter engajada com a vida acadêmica. | Lista cronológica com data, local e organizador; a descrição informa como se inscrever. | RF12 |
| **US12** | Usuária | Como usuária, desejo salvar e remover eventos da minha agenda no app, para não esquecer compromissos. | Botão "Salvar" no evento e aba "Salvos" com opção de remover. | RF12 |

## 5. Módulo: Acolhimento (Segurança Psicológica)

| ID | Persona | História de Usuário | Critério de Aceite | RF |
| :--- | :--- | :--- | :--- | :--- |
| **US13** | Usuária | Como usuária, desejo postar relatos ou dúvidas no fórum de forma anônima, para compartilhar vulnerabilidades sem medo de julgamento. | Chave "Postar como anônima" que substitui nome e foto por um avatar genérico antes de publicar. | RF13 |
| **US14** | Usuária | Como usuária, desejo denunciar postagens inadequadas, para ajudar a manter o ambiente seguro e colaborativo. | Modal com motivos de seleção única para a denúncia. | RF16 |

## 6. Módulo: Administrativo (Gestão Meninas Digitais)

| ID | Persona | História de Usuário | Critério de Aceite | RF |
| :--- | :--- | :--- | :--- | :--- |
| **US15** | Admin | Como gestora, desejo cadastrar e manter perfis inspiradores, para manter a galeria atualizada. | Formulário com biografia, área, conquistas e link; opção de publicar agora ou salvar como inativo. | RF15 |
| **US16** | Admin | Como gestora, desejo publicar eventos de interesse da comunidade, para centralizar as informações para as alunas em STEM. | Agenda administrativa com botão (+) "Criar evento", edição e rascunho. | RF15 |
| **US17** | Admin | Como moderadora, desejo avaliar as denúncias e remover postagens inadequadas, para manter o ambiente de acolhimento seguro. | Painel de denúncias com detalhes do post, ações "Ignorar" e "Excluir" e confirmação da exclusão. | RF16 |
| **US18** | Admin | Como gestora, desejo visualizar o número total de usuárias e de mentorias, para reportar o impacto do projeto. | Dashboard com métricas na tela inicial administrativa. | RF14 |
| **US20** | Admin | Como gestora, desejo consultar o histórico de conduta de uma usuária e enviar aviso ou suspender seu acesso, para zelar pela convivência na comunidade. | Detalhes da usuária com atividade e conduta; ações "Enviar aviso" e "Suspender acesso", ambas com confirmação. | RF17 |

> **Nota de Validação:** as histórias foram testadas no protótipo interativo de alta fidelidade com fluxo guiado (ver `results/`). Na proposta, previa-se um protótipo de média fidelidade com a técnica Mágico de Oz.