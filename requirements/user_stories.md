# 👥 Histórias de Usuário (User Stories) - Rede Delas

Este documento detalha as necessidades das usuárias e os critérios de aceite para a validação do protótipo Rede Delas, servindo como guia para o design de interação no Figma.

## 1. Infraestrutura e Acesso (Core)

| ID | Persona | História de Usuário (User Story) | Critério de Aceite |
| :--- | :--- | :--- | :--- |
| **US01** | Visitante | Como estudante da UTFPR, desejo me cadastrar no app usando meu e-mail institucional, para garantir que a rede seja exclusiva para a comunidade acadêmica. | Validação estrita do domínio `@alunos.utfpr.edu.br` no formulário de cadastro. |
| **US02** | Usuária | Como usuária cadastrada, desejo realizar login com senha ou recuperar meu acesso via e-mail, para proteger meus dados e conexões. | Tela de login funcional e fluxo de "Esqueci minha senha" com feedback de envio. |
| **US03** | Usuária | Como usuária, desejo configurar meu perfil (foto, curso, período e bio), para que outras alunas me identifiquem corretamente na rede. | Interface de edição de perfil com campos obrigatórios e upload de avatar. |
| **US04** | Veterana | Como aluna avançada, desejo sinalizar minha disponibilidade como mentora, para que calouras possam me encontrar para tirar dúvidas. | Chave (Toggle) "Disponível para Mentoria" visível no perfil. |

## 2. Módulo: Elas Inspiram (Role Models)

| ID | Persona | História de Usuário | Critério de Aceite |
| :--- | :--- | :--- | :--- |
| **US05** | Estudante | Como usuária, desejo navegar por uma galeria de perfis inspiradores, para conhecer a trajetória de mulheres de sucesso em STEM. | Lista em grid com foto, nome, cargo e área de atuação. |
| **US06** | Estudante | Como usuária, desejo salvar perfis inspiradores como "favoritos", para acessá-los rapidamente em momentos de desmotivação. | Ícone de estrela que move o perfil para uma aba específica de "Favoritas". |

## 3. Módulo: Conexões (Mentoria Peer-to-Peer)

| ID | Persona | História de Usuário | Critério de Aceite |
| :--- | :--- | :--- | :--- |
| **US07** | Caloura | Como aluna, desejo filtrar mentoras por disciplinas específicas (ex: Cálculo I), para encontrar ajuda técnica pontual. | Campo de busca funcional que filtra a lista de veteranas por "tags" de competência. |
| **US08** | Caloura | Como aluna, desejo enviar uma solicitação de mentoria descrevendo minha dúvida, para iniciar um canal de conversa com uma veterana. | Botão "Solicitar Ajuda" que abre um modal para entrada de texto de dúvida inicial. |
| **US09** | Mentora | Como mentora, desejo visualizar os detalhes da dúvida e o perfil da solicitante antes de aceitar, para gerenciar minha capacidade de apoio. | Painel de "Pedidos Pendentes" exibindo a mensagem enviada pela aluna. |
| **US10** | Usuária | Como usuária, desejo avaliar a experiência de mentoria ao final do ciclo, para contribuir com a melhoria da rede. | Modal de finalização com escala de 5 estrelas e campo de comentário. |

## 4. Módulo: Comunidade (Agenda Acadêmica)

| ID | Persona | História de Usuário | Critério de Aceite |
| :--- | :--- | :--- | :--- |
| **US11** | Usuária | Como usuária, desejo visualizar uma agenda centralizada de eventos (palestras, workshops), para me manter engajada com a vida acadêmica. | Lista cronológica com data, local e informações do organizador (CAs, DAs, MD). |
| **US12** | Usuária | Como usuária, desejo salvar um evento no meu calendário pessoal do app, para receber lembretes e não esquecer compromissos. | Botão "Salvar na Agenda" que gera uma marcação visual de "Lembrete Ativo". |

## 5. Módulo: Acolhimento (Segurança Psicológica)

| ID | Persona | História de Usuário | Critério de Aceite |
| :--- | :--- | :--- | :--- |
| **US13** | Usuária | Como usuária, desejo postar relatos ou dúvidas no fórum de forma anônima, para compartilhar vulnerabilidades sem medo de julgamento. | Componente Toggle Switch que substitui nome e foto por um avatar genérico. |
| **US14** | Usuária | Como usuária, desejo denunciar postagens inadequadas, para ajudar a manter o ambiente seguro e colaborativo. | Modal com opções de múltipla escolha (Radio Buttons) para selecionar o motivo da denúncia. |

## 6. Módulo: Administrativo (Gestão Meninas Digitais)

| ID | Persona | História de Usuário | Critério de Aceite |
| :--- | :--- | :--- | :--- |
| **US15** | Admin | Como gestora, desejo cadastrar novas Role Models e professoras, para manter a galeria de inspiração sempre atualizada. | Formulário de CRUD exclusivo com campos para biografia e LinkedIn. |
| **US16** | Admin | Como gestora, desejo publicar editais e eventos de interesse da comunidade, para centralizar as informações para as alunas em STEM. | Dashboard administrativo com botão (+) "Novo Evento". |
| **US17** | Admin | Como moderadora, desejo remover postagens inadequadas do fórum, para manter o ambiente de acolhimento ético e saudável. | Ícone de lixeira visível apenas para Admin com modal de justificativa de exclusão. |
| **US18** | Admin | Como gestora, desejo visualizar o número total de mentorias e usuárias, para reportar o impacto social do projeto à UTFPR. | Dashboard de métricas com contadores numéricos na tela inicial administrativa. |

> **Nota de Validação:** Todas as histórias acima serão testadas no protótipo de média-fidelidade utilizando a técnica Mágico de Oz para simular o comportamento do sistema.