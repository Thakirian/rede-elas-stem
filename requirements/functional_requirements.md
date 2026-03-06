# Requisitos Funcionais (RF) - Rede Elas@STEM

Este documento detalha as funcionalidades essenciais e as especificações técnicas para a operação da plataforma.

## 1. Tabela de Requisitos

| ID | Funcionalidade | Prioridade |
| :--- | :--- | :--- |
| **RF01** | Cadastro de usuárias com dados pessoais e acadêmicos (e-mail institucional) | Essencial |
| **RF02** | Autenticação de usuárias (Login e Recuperação de Senha) | Essencial |
| **RF03** | Edição e Gerenciamento de Perfil de Usuária | Essencial |
| **RF04** | Visualização da Home com resumo de novidades e atalhos | Alta |
| **RF05** | Listagem e detalhamento de perfis inspiradores (Role Models) | Alta |
| **RF06** | Sistema de favoritar perfis no módulo 'Elas Inspiram' | Média |
| **RF07** | Busca e filtragem de mentoras por disciplinas específicas | Essencial |
| **RF08** | Envio de solicitações de mentoria com notificação | Alta |
| **RF09** | Gestão de solicitações (Aceitar/Recusar) no perfil da mentora | Alta |
| **RF10** | Visualização de agenda centralizada de eventos acadêmicos | Alta |
| **RF11** | Salvamento de eventos em calendário pessoal (Agenda do App) | Média |
| **RF12** | Fórum de acolhimento com suporte a postagens anônimas | Essencial |
| **RF13** | Moderação de conteúdo e exclusão de postagens (Perfil Admin) | Essencial |

## 2. Detalhamento Técnico (Especificação)

* **Acesso (RF01 & RF02):** Validação obrigatória do domínio `@alunos.utfpr.edu.br`.
* **Perfil (RF03):** Edição de interesses e biografia; configuração de disponibilidade para mentoria.
* **Inspiração (RF05 & RF06):** Cards com biografia completa e armazenamento do ID do perfil nos "favoritos".
* **Mentoria (RF07, RF08 & RF09):** Sistema de "pendência" que bloqueia o chat até o aceite da mentora.
* **Comunidade (RF10 & RF11):** Eventos com título, data, local e link de inscrição; lembrete visual no app.
* **Anonimato (RF12):** Uso de *toggle* para mascarar identidade como "Usuária Anônima".
* **Moderação (RF13):** Painel administrativo para as administradoras (Meninas Digitais).