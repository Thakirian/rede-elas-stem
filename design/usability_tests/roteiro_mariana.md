# 📱 Documentação de Teste de Usabilidade 02 — Fluxo Mentora (Mariana)

**Métricas Globais:** Duração ~43 min | Google Meet (Gravação Tela/Voz)
**Foco Metodológico:** Gestão de mentoria, tomada de decisão, perspectiva mentora.

---

### TAREFA 1 · Login — Acesso com Conta Existente (Core | 2 min)
**Contexto:** Verificar se o caminho de “já sou cadastrada” é claro. Não há onboarding.
**Roteiro:** *"A Mariana já tem uma conta no Rede Delas. Acesse o aplicativo e entre na sua conta."*
**Caminho:** `Tela 01 Login` → `Campos pré-preenchidos` → `Entrar` → `Tela 06 Home` ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Entrou na Home sem ajuda.<br>**⚠️ Parcial:** Tentou “Cadastre-se” antes.<br>**❌ Falhou:** Não conseguiu acessar. | - [ ] Foi direto para "Entrar" ou errou?<br>- [ ] Comentou do e-mail institucional?<br>- [ ] Tempo de acesso: ___ segundos |
> *Nota: Se tocar em "Cadastre-se", deixe perceber o erro sozinha para validar a hierarquia visual.*

---

### TAREFA 2 · Exploração da Home (Home | 2 min)
**Contexto:** Tarefa de observação (IHC). Validar se a interface comunica o contexto da veterana.
**Roteiro:** *"Não clique em nada ainda. Analise a tela, role para baixo devagar e me diga: só de olhar, o que acha que é possível fazer no aplicativo?"*
**Caminho:** `Tela 06 Home` → Scroll vertical livre → Análise visual ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Citou ≥ 3 itens, incluindo mentoria.<br>**⚠️ Parcial:** Citou 1 a 2 funcionalidades.<br>**❌ Falhou:** Não inferiu o uso do app. | - [ ] Ordem: 1º _____, 2º _____, 3º _____<br>- [ ] Identificou o card de mentoria rápido?<br>- [ ] Comentou algo diferente da caloura? |

---

### TAREFA 3 · Elas Inspiram — Explorar e Favoritar (Inspiram | 4 min)
**Contexto:** Validar a consistência da experiência entre perfis diferentes.
**Roteiro:** *"Explore os perfis. Encontre a Margaret Hamilton, leia a história e acesse o link externo. Adicione-a às favoritas, e depois remova ela de lá."*
**Caminho:** `TabBar` → `Tela 07` → `Card Margaret` → `História Completa` → `Link Relevante` → `Favoritar (Estrela)` → `Aba Favoritas (Tela 09)` → `Desfavoritar` ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Completou os 4 passos do fluxo.<br>**⚠️ Parcial:** Fez 2 ou 3 passos.<br>**❌ Falhou:** Travou antes de achar a lista. | - [ ] Tempo para achar Margaret: ___ seg.<br>- [ ] Achou a aba "Favoritas" sem dicas?<br>- [ ] Leu a história antes de favoritar? |

---

### TAREFA 4 · Recusar Julia, Aceitar Luana e Match (Conexões | 5 min)
**Contexto:** Gerenciamento de pedidos. A recusa faz o card sumir; o aceite avança para o Match.
**Roteiro 1 (Recusa):** *"Você recebeu pedidos. Há um da Julia sobre Lógica, mas você não domina o assunto agora. O que faria?"*
**Roteiro 2 (Aceite):** *"Restou o pedido da Luana sobre Algoritmos. Leia com atenção e decida."*
**Caminho:** `TabBar Conexões` → `Minhas Mentorias (Pendentes)` → `Recusar Julia` → Card some ✅ → `Card Luana (Detalhes)` → `Aceitar Mentoria` → `Tela Match` → `Iniciar Conversa` ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Recusou Julia, leu detalhes e aceitou Luana.<br>**⚠️ Parcial:** Aceitou sem ler os detalhes.<br>**❌ Falhou:** Não achou o painel de mentorias. | - [ ] Recusou direto da lista ou abriu detalhes?<br>- [ ] Leu o contexto da Luana (1º período)?<br>- [ ] Reagiu espontaneamente à tela de Match? |

---

### TAREFA 5 · Chat como Mentora e Finalizar (Conexões | 3 min)
**Contexto:** Papéis invertidos no chat. Mariana finaliza e vê a avaliação recebida.
**Roteiro:** *"Você está no chat com a Luana. Role para ver o histórico. Quando sentir que acabou, encerre a mentoria."*
**Caminho:** `Chat Mentora` → Scroll leitura ✅ → `3 Pontos (Header)` → `Finalizar Mentoria` → `Modal (Vê 5 Estrelas)` → `Concluir e Salvar` → `Resumo` ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Leu o chat, finalizou e viu avaliação.<br>**⚠️ Parcial:** Finalizou mas não notou a nota.<br>**❌ Falhou:** Não achou "Finalizar" nos 3 pontos. | - [ ] Notou que balões estão invertidos?<br>- [ ] Hesitou nos 3 pontos? (Tempo: ___ seg).<br>- [ ] Reagiu ao ver as 5 estrelas recebidas? |

---

### TAREFA 6 · Verificar Histórico Completo (Conexões | 3 min)
**Contexto:** Validar se o sistema exibe tanto aceites (Luana) quanto recusas (Julia).
**Roteiro:** *"Onde verificaria o resumo de TODAS as suas interações, tanto a concluída quanto a recusada?"*
**Caminho:** `Resumo` → `Voltar (Seta)` → `Tela 13 Minhas Mentorias` → `Aba Concluídas` → Vê os 2 cards ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Encontrou aba e viu os dois cards.<br>**⚠️ Parcial:** Encontrou mas viu só 1 registro.<br>**❌ Falhou:** Não encontrou o histórico. | - [ ] Achou a sub-aba "Concluídas"?<br>- [ ] Notou o status "Não iniciada" da Julia?<br>- [ ] Comentou a diferença entre os cards? |

---

### TAREFA 7 · Fórum — Publicar Anônimo e Editar (Fórum | 4 min)
**Contexto:** Lógica inversa à da Luana (Posta anônima → Edita para com nome).
**Roteiro 1:** *"Compartilhe uma dica para as calouras, mas publique sem revelar seu nome (anônima)."*
**Roteiro 2:** *"Mudou de ideia: quer que saibam que foi você. Edite para colocar seu nome."*
**Caminho:** `Fórum` → `Novo Relato` → `Ativa Toggle` → `Publicar` ✅ → `Feed` → `3 Pontos (Post dela)` → `Editar` → `Desativa Toggle` → `Salvar` ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Publicou anônimo e editou com sucesso.<br>**⚠️ Parcial:** Fez só 1 dos momentos.<br>**❌ Falhou:** Não achou o toggle ou menu editar. | - [ ] Achou os 3 pontos no próprio post?<br>- [ ] Percebeu que privacidade muda via edição?<br>- [ ] Notou a foto voltando no feed? |

---

### TAREFA 8 · Fórum — Explorar e Denunciar (Fórum | 3 min)
**Contexto:** Avaliação da moderação descentralizada de conteúdo de terceiros.
**Roteiro:** *"Explore o feed. Se encontrar um post hostil contra as regras, o que faria?"*
**Caminho:** `Feed` → Encontra post hostil → `3 Pontos (Outra usuária)` → `Denunciar` → `Seleciona Motivo` → `Enviar` ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Encontrou post hostil e denunciou.<br>**⚠️ Parcial:** Achou os 3 pontos mas não enviou.<br>**❌ Falhou:** Não achou menu de terceiros. | - [ ] Diferenciou o menu dela para o de terceiros?<br>- [ ] Tentou curtir antes? (Não funciona).<br>- [ ] O modal de motivos foi claro? |

---

### TAREFA 9 · Descobrir e Salvar Evento (Comunidade | 2 min)
**Contexto:** Consistência de interface (mesma ação da Luana).
**Roteiro:** *"Encontre a 'Aula de Defesa Pessoal' nos eventos e salve para não esquecer."*
**Caminho:** `TabBar Eventos` → `Aula de Defesa Pessoal` → `Salvar (Bookmark)` → `Minha Agenda` ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Encontrou, abriu detalhes e salvou.<br>**⚠️ Parcial:** Encontrou mas não soube salvar.<br>**❌ Falhou:** Não achou módulo/evento. | - [ ] Tempo para achar o evento: ___ seg.<br>- [ ] Associou a bandeira a "salvar"?<br>- [ ] Conferiu a agenda espontaneamente? |

---

### TAREFA 10 · Perfil, Toggle Mentora e Logout (Gestão | 4 min)
**Contexto:** Perfil possui métricas diferentes e a feature crítica: pausar mentoria. Logout é direto na tela.
**Roteiro 1:** *"Acesse seu perfil. Explique o que vê nele."*
**Roteiro 2:** *"Está sobrecarregada e quer pausar novos pedidos de mentoria. Como faria?"*
**Roteiro 3:** *"Encontre a opção de encerrar sua sessão, o app vai zerar."*
**Caminho:** `Avatar MC` → `Meu Perfil` (verbaliza badges) ✅ → `Editar Perfil` → `Desativa Toggle "Disponível"` → `Salvar` ✅ → `Meu Perfil` → `Sair da Conta (Botão Vermelho)` → `Login` ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Explicou perfil, achou toggle e deslogou.<br>**⚠️ Parcial:** Falhou em 1 das 3 partes.<br>**❌ Falhou:** Não achou o perfil/toggle crítico. | - [ ] Notou os badges de conquista?<br>- [ ] Achou o toggle de mentora rápido?<br>- [ ] Hesitou no botão vermelho de Sair? |

---

### EXTRA · Exploração Livre pós-Logout (2 a 3 min)
**Contexto:** Mapeamento livre para comparar o interesse da Mentora vs. Mentoranda.
**Roteiro:** *"Teste finalizado! Vou te dar 2 minutinhos na tela de login. Entre e explore o app livremente, só pense alto."*

* **O que registrar:**
  - 1º Clique: _______________ | 2º Clique: _______________ | 3º Clique: _______________
  - Frustrações com cliques, comentários gerais e comparações com a jornada da caloura.