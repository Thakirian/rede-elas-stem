# 📝 Requisitos Funcionais (RF) - Rede Delas

Este documento detalha as funcionalidades essenciais e as especificações técnicas para a operação da plataforma Rede Delas, cobrindo as necessidades das estudantes (mentorandas e mentoras) e da equipe de gestão (administradoras).

Os requisitos foram derivados dos achados do Mapeamento Sistemático da Literatura (pasta slm/). Os elementos que surgiram durante a prototipação e que não decorrem do mapeamento estão na Seção 3.

## 1. Tabela de Requisitos

| ID | Funcionalidade | Persona | Prioridade |
| :--- | :--- | :--- | :--- |
| **RF01** | Cadastro via e-mail institucional (@alunos.utfpr.edu.br) | Visitante | Essencial |
| **RF02** | Autenticação (login) e recuperação de senha | Usuária | Essencial |
| **RF03** | Configuração e edição de perfil (biografia, curso, período e interesses) | Usuária | Essencial |
| **RF04** | Habilitação da função de mentora (chave "Desejo ser mentora") | Usuária | Essencial |
| **RF05** | Home com resumo dinâmico (inspiradora do dia, mentoria, eventos e fórum) | Usuária | Alta |
| **RF06** | Galeria de perfis inspiradores (Role Models) | Usuária | Alta |
| **RF07** | Detalhamento da trajetória e favoritação de perfis inspiradores | Usuária | Média |
| **RF08** | Busca e filtragem de mentoras por disciplina | Mentoranda | Essencial |
| **RF09** | Solicitação de mentoria com mensagem de dúvida e acompanhamento do pedido | Mentoranda | Alta |
| **RF10** | Painel de gestão de pedidos (aceitar, recusar e finalizar) | Mentora | Alta |
| **RF11** | Chat seguro (liberado apenas após o aceite) | Mentoranda e mentora | Essencial |
| **RF12** | Agenda de eventos acadêmicos: consulta e gestão da agenda pessoal (salvar e remover eventos) | Usuária | Alta |
| **RF13** | Fórum de acolhimento com postagem anônima | Usuária | Essencial |
| **RF14** | Dashboard de métricas de impacto (total de usuárias e de mentorias) | Admin | Média |
| **RF15** | Gestão de conteúdo (cadastro, edição, publicação e exclusão de perfis inspiradores e de eventos) | Admin | Alta |
| **RF16** | Moderação de conteúdo (denúncia por usuárias e exclusão por Admin) | Usuária e Admin | Essencial |
| **RF17** | Gestão de usuárias (envio de aviso e suspensão de acesso) | Admin | Alta |

## 2. Detalhamento Técnico (Especificação)

- **Acesso e segurança (RF01 e RF02):** o cadastro é restrito à comunidade da UTFPR-CP e exige e-mail do domínio @alunos.utfpr.edu.br. A recuperação de senha ocorre por link enviado ao e-mail institucional. No protótipo, a validação do domínio e o envio do e-mail são simulados.
- **Identidade (RF03 e RF04):** a usuária gerencia como é vista na rede (foto, biografia, curso, período e interesses). A chave "Desejo ser mentora", presente no cadastro e na edição do perfil, habilita a função de mentora e pode ser desativada a qualquer momento. Enquanto estiver ativa, as disciplinas do perfil incluem a usuária nos resultados de busca de mentoras.
- **Home (RF05):** reúne a inspiradora do dia, o campo de postagem no fórum, o status da mentoria, os próximos eventos e o resumo de atividade do fórum.
- **Módulo Elas Inspiram (RF06 e RF07):** galeria de perfis com busca e filtros por categoria (alunas, professoras e egressas). O detalhe traz trajetória, conquistas e link externo (LinkedIn ou outro). A usuária pode favoritar e remover perfis da lista de favoritas. A manutenção do conteúdo cabe à Admin (RF15).
- **Módulo Conexões (RF08 a RF11):** a busca filtra mentoras por disciplina. A solicitação inclui uma mensagem de dúvida, cria um pedido pendente e pode ser acompanhada por status (pendentes, em andamento e concluídas) e cancelada pela mentoranda. A mentora aceita ou recusa, com confirmação da recusa. O chat só é liberado após o aceite. Ambas podem finalizar a mentoria: a mentoranda avalia (estrelas e comentário), e a mentora encerra sem atribuir nota e visualiza a avaliação recebida no resumo.
- **Módulo Comunidade (RF12):** centraliza eventos de centros acadêmicos, diretórios, coordenação e projetos de extensão. O detalhe informa título, data, local, organizador e, na descrição, a forma de inscrição (link ou contato com o responsável). O aplicativo não realiza inscrição. A usuária salva e remove eventos de sua agenda pessoal.
- **Módulo Acolhimento (RF13 e RF16):** fórum organizado por categorias de apoio. A chave "Postar como anônima" substitui nome e foto por um avatar genérico antes da publicação e pode ser alterada na edição do relato. A autora edita e exclui o próprio relato, e a usuária pode ocultar ou denunciar posts de terceiros, escolhendo um motivo. A Admin avalia as denúncias e decide por ignorar ou excluir, com confirmação.
- **Painel administrativo (RF14 a RF17):** o dashboard mostra métricas e pendências. A Admin cadastra, edita, publica (ou salva como rascunho) e exclui perfis inspiradores e eventos. Na gestão