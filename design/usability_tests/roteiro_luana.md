# 📱 Documentação de Teste de Usabilidade 01 — Fluxo Mentoranda (Luana)

**Métricas Globais:** Duração ~42 min | Google Meet (Gravação Tela/Voz)
**Foco Metodológico:** Acolhimento, busca por ajuda, privacidade (RF12) e moderação (RF13).

---

### TAREFA 1 · Cadastro e Primeiro Acesso (Core | 3 min)
**Contexto:** Avaliar a autoexplicação do onboarding. O protótipo possui dados simulados.
**Roteiro:** *"Imagine que você acabou de ouvir falar do Rede Delas no grupo de calouros. Crie sua conta e siga o fluxo até a tela inicial. Os campos já estão preenchidos, você só precisa avançar."*
**Caminho:** `Tela 01 Login` → `Cadastre-se` → `Tela 02` → `Próximo` → `Tela 03` → `Concluir` → `Tela 06 Home` ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Home alcançada sem ajuda.<br>**⚠️ Parcial:** Hesitação > 30s ou 1 pergunta.<br>**❌ Falhou:** Precisou de intervenção direta. | - [ ] Achou "Cadastre-se" sem hesitar?<br>- [ ] Compreendeu os passos (1 de 2)?<br>- [ ] Comentou do toggle de mentora? |
> *Nota: Aguardar até 2 minutos caso haja travamento na tela inicial antes de intervir.*

---

### TAREFA 2 · Exploração da Home (Home | 2 min)
**Contexto:** Tarefa de observação pura (IHC). Mede a compreensão da hierarquia visual sem instruções de clique.
**Roteiro:** *"Não clique em nada ainda. Analise a tela, role para baixo devagar e me diga em voz alta: só de olhar, o que você acha que é possível fazer nesse aplicativo?"*
**Caminho:** `Tela 06 Home` → Scroll vertical livre → Análise visual ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Citou ≥ 3 funcionalidades.<br>**⚠️ Parcial:** Citou 1 a 2 funcionalidades.<br>**❌ Falhou:** Não inferiu o uso do app. | - [ ] Qual a ordem exata do que ela viu/falou?<br>- [ ] Mencionou Fórum, Eventos e Mentoria?<br>- [ ] Olhou a TabBar no rodapé? |

---

### TAREFA 3 · Elas Inspiram — Explorar e Favoritar (Inspiram | 4 min)
**Contexto:** Validar a leitura profunda e a microinteração funcional no perfil da Margaret Hamilton.
**Roteiro:** *"Explore os perfis disponíveis. Encontre a Margaret Hamilton, abra o perfil, leia a história e acesse o link externo. Depois, adicione-a às favoritas, vá até a sua lista e remova esse perfil de lá."*
**Caminho:** `TabBar` → `Tela 07` → `Card Margaret` → `História Completa` → `Link Relevante` → `Favoritar (Estrela)` → `Aba Favoritas (Tela 09)` → `Desfavoritar` ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Completou os 4 passos do fluxo.<br>**⚠️ Parcial:** Fez 2 ou 3 passos.<br>**❌ Falhou:** Travou antes de achar a lista. | - [ ] Entendeu que o botão abre link externo?<br>- [ ] Achou a aba "Favoritas" sem dicas?<br>- [ ] Descobriu como remover o favorito? |

---

### TAREFA 4 · Solicitar Mentoria e Acompanhar Status (Conexões | 4 min)
**Contexto:** Primeira fase do fluxo principal. Localizar a mentora alvo e testar o modal de envio.
**Roteiro:** *"Você está travada em Algoritmos. Procure a Mariana Costa e envie um pedido de mentoria. Depois, como você verificaria se o seu pedido está aguardando resposta?"*
**Caminho:** `TabBar` → `Tela 10A Explorar` → `Card Mariana` → `Solicitar Mentoria` → `Enviar` → `Tela 12 (Feedback)` → `Aba Pendentes` ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Enviou e verificou status pendente.<br>**⚠️ Parcial:** Enviou, mas não checou o status.<br>**❌ Falhou:** Não encontrou as Conexões. | - [ ] Usou busca ou rolagem para achar Mariana?<br>- [ ] O modal de sobreposição foi intuitivo?<br>- [ ] Achou a aba de status pendente sozinha? |

---

### TAREFA 5 · Chat, Finalização e Avaliação (Conexões | 5 min)
**Contexto:** Simulação de passagem de tempo. Teste de descobrimento de menu oculto (3 pontos) e sistema de *rating*.
**Roteiro:** *"Imagine que horas se passaram e a Mariana aceitou. Encontre essa mentoria ativa, entre no chat e, supondo que a dúvida foi resolvida, encerre a mentoria, dê uma nota e verifique o histórico."*
**Caminho:** `Aba Em Andamento` → `Chat` → `3 Pontos` → `Finalizar Mentoria` → `5 Estrelas` → `Concluir e Salvar` → `Aba Concluídas` ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Avaliou e verificou nas concluídas.<br>**⚠️ Parcial:** Encerrou mas não checou histórico.<br>**❌ Falhou:** Não encontrou o chat/botão finalizar. | - [ ] Achou o menu oculto nos 3 pontos?<br>- [ ] Hesitou na hora de finalizar? (Cronometre).<br>- [ ] O modal de avaliação transmitiu clareza? |

---

### TAREFA 6 · Toggle de Anonimato e Vitória (Fórum | 5 min)
**Contexto:** Teste do RF12. Se o toggle de privacidade falhar na visibilidade, causa erro crítico de segurança psicológica.
**Roteiro:** *"1. Poste um desabafo no fórum, mas de forma que ninguém saiba quem é você (anônima). 2. Depois, poste sua vitória com o seu nome aparecendo."*
**Caminho:** `Fórum` → `Novo Relato` → `Ativa Toggle` → `Publicar` → `Novo Relato (Vitória)` → `Toggle Desativado` → `Publicar` ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Postou anônima e depois identificada.<br>**⚠️ Parcial:** Fez apenas 1 dos fluxos corretamente.<br>**❌ Falhou:** Não descobriu o funcionamento do toggle. | - [ ] Percebeu a mutação de cor/foto no toggle?<br>- [ ] Publicou o segundo post com nome ciente?<br>- [ ] Comentou algo sobre se sentir segura? |

---

### TAREFA 7 · Excluir Post e Denunciar (Fórum | 4 min)
**Contexto:** Validar Heurística de Controle (reversão de ação) e moderação descentralizada de terceiros.
**Roteiro:** *"1. Você mudou de ideia, apague o relato anônimo que publicou. 2. Explore o feed, se achar um post hostil, o que faria?"*
**Caminho:** `Feed` → `3 pontos (Post Próprio)` → `Excluir` → `Confirmar` → `3 pontos (Terceiro)` → `Denunciar` → `Modal de Motivo` ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Excluiu com sucesso e fez a denúncia.<br>**⚠️ Parcial:** Concluiu apenas exclusão ou denúncia.<br>**❌ Falhou:** Não localizou os menus contextuais. | - [ ] Entendeu que o anônimo ainda era editável?<br>- [ ] Diferenciou menu próprio vs terceiros?<br>- [ ] Entendeu as opções de denúncia? |

---

### TAREFA 8 · Descobrir e Salvar Evento (Comunidade | 3 min)
**Contexto:** Interação com informações institucionais verídicas e agendamento interno.
**Roteiro:** *"Dê uma olhada nos eventos. Encontre a 'Aula de Defesa Pessoal' e salve esse evento para não esquecer."*
**Caminho:** `TabBar Eventos` → `Card Defesa Pessoal` → `Detalhes` → `Salvar (Bookmark)` → `Aba Minha Agenda` ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Encontrou, abriu detalhes e salvou.<br>**⚠️ Parcial:** Encontrou mas não soube salvar.<br>**❌ Falhou:** Não achou o módulo ou evento. | - [ ] Usou atalho da Home ou a TabBar?<br>- [ ] Associou o ícone de bandeira/bookmark a salvar?<br>- [ ] Conferiu a agenda por conta própria? |

---

### TAREFA 9 · Central de Notificações (Gestão | 2 min)
**Contexto:** Avaliar modelo mental sobre onde buscar feedback consolidado do sistema.
**Roteiro:** *"Lembra de tudo que fez até agora? Como você verificaria se tem algum aviso do sistema sobre essas coisas?"*
**Caminho:** `Header (Topo)` → `Sino` → `Lê Notificações (Mentoria/Fórum)` ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Achou o sino e leu os feedbacks.<br>**⚠️ Parcial:** Achou, mas não conectou com as tarefas.<br>**❌ Falhou:** Procurou no lugar errado. | - [ ] Foi direto ao sino no topo?<br>- [ ] Entendeu a diferença visual de lida/não-lida? |

---

### TAREFA 10 · Perfil, Histórico e Logout (Gestão | 5 min)
**Contexto:** Exploração não-guiada de métricas e encerramento da sessão simulada.
**Roteiro:** *"Acesse seu perfil e me explique o que vê nele. (Aguarda). Como isso é um protótipo, tudo vai zerar. Encontre a opção de sair da conta."*
**Caminho:** `Avatar LR` → `Meu Perfil` → `Minha Atividade (Abas)` → `Configurações` → `Sair da Conta` ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Achou histórico, explicou e deslogou.<br>**⚠️ Parcial:** Deslogou sem analisar o histórico.<br>**❌ Falhou:** Não achou a saída ou o perfil. | - [ ] Achou "Minha Atividade" sozinha?<br>- [ ] Hesitou no botão destrutivo de Sair da Conta? |

---

### EXTRA · Exploração Livre pós-Logout (2 a 3 min)
**Contexto:** Mapeamento livre de interesse e rotas naturais sem viés de tarefa imposta.
**Roteiro:** *"O teste acabou! Mas vou te dar 2 minutinhos na tela inicial. Entre e navegue livremente por onde quiser, só continue pensando alto."*

* **O que registrar:**
  - 1º Clique: _______________ | 2º Clique: _______________ | 3º Clique: _______________
  - Comentários finais, expressões de frustração ou alívio sobre a interface.