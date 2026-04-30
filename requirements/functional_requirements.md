# 📝 Requisitos Funcionais (RF) - Rede Delas

Este documento detalha as funcionalidades essenciais e as especificações técnicas para a operação da plataforma Rede Delas, cobrindo as necessidades das estudantes (mentorandas/mentoras) e da equipe de gestão (administradoras).

## 1. Tabela de Requisitos

| ID | Funcionalidade | Persona | Prioridade |
| :--- | :--- | :--- | :--- |
| **RF01** | Cadastro via e-mail institucional (@alunos.utfpr.edu.br) | Visitante | Essencial |
| **RF02** | Autenticação (Login) e Fluxo de Recuperação de Senha | Usuária | Essencial |
| **RF03** | Configuração de Perfil (Bio, Curso, Período e Interesses) | Usuária | Essencial |
| **RF04** | Habilitação da Função Mentora (Toggle "Disponível para Ajuda") | Usuária | Essencial |
| **RF05** | Home com Resumo Dinâmico (Novidades, Eventos e Mentoria) | Usuária | Alta |
| **RF06** | Galeria de Perfis Inspiradores (Role Models) | Usuária | Alta |
| **RF07** | Detalhamento de Trajetória e Favoritar Inspiradoras | Usuária | Média |
| **RF08** | Busca e Filtragem de Mentoras por Disciplina Específica | Mentoranda | Essencial |
| **RF09** | Envio de Solicitação de Mentoria com Mensagem de Dúvida | Mentoranda | Alta |
| **RF10** | Painel de Gestão de Pedidos (Aceitar/Recusar/Finalizar) | Mentora | Alta |
| **RF11** | Chat Seguro (Liberado apenas após o "Match") | Ambas | Essencial |
| **RF12** | Agenda Centralizada de Eventos (CAs, DAs, Coordenação) | Usuária | Alta |
| **RF13** | Calendário Pessoal (Eventos Salvos e Lembretes) | Usuária | Média |
| **RF14** | Fórum de Acolhimento com Toggle de Anonimato | Usuária | Essencial |
| **RF15** | Dashboard de Métricas de Impacto (Total de Usuárias/Mentorias) | Admin | Média |
| **RF16** | Gestão de Conteúdo (CRUD de Role Models e Eventos) | Admin | Alta |
| **RF17** | Moderação Ativa e Exclusão de Postagens Inadequadas | Admin | Essencial |

## 2. Detalhamento Técnico (Especificação)

* **Acesso e Segurança (RF01 & RF02):** Restrição de acesso à comunidade da UTFPR-CP. O sistema deve validar o domínio do e-mail. A recuperação de senha será simulada via interface de feedback por e-mail.
* **Gestão de Identidade (RF03 & RF04):** Permite que a usuária gerencie como é vista na rede. O sistema utiliza as disciplinas marcadas como "domínio" para incluí-la nos resultados de busca de mentoras quando o toggle de disponibilidade estiver ativo.
* **Módulo Inspiram (RF06, RF07 & RF16):** As Role Models são exibidas em uma galeria visual. O detalhamento inclui links externos (LinkedIn) e badges de conquista. A Administradora é responsável pela manutenção deste conteúdo.
* **Módulo Conexões (RF08, RF09, RF10 & RF11):** O motor de busca filtra mentoras por strings de disciplinas técnicas. A solicitação cria um registro de pendência. O chat só é instanciado no sistema após a confirmação positiva da mentora.
* **Módulo Comunidade (RF12, RF13 & RF16):** Centraliza avisos institucionais e estudantis. O salvamento na agenda pessoal cria um filtro de exibição para "Meus Eventos".
* **Módulo Acolhimento (RF14 & RF17):** Fórum baseado em categorias de suporte psicossocial. O anonimato é garantido por um interruptor que desvincula o ID da usuária da exibição pública do post. A Admin possui permissão de remoção definitiva para garantir a segurança do ambiente.

> **Nota Metodológica:** Para fins do protótipo de média-fidelidade (MFi), as funcionalidades que exigem persistência em banco de dados serão simuladas através da técnica Mágico de Oz.