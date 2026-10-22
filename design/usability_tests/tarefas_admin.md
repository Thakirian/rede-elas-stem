# 📱 Documentação de Teste de Usabilidade 03 — Fluxo Admin (Gestão)

**Métricas Globais:** Duração ~38 min | Google Meet (Gravação Tela/Voz)
**Foco Metodológico:** Gestão de conteúdo, moderação, governança e tomada de decisão crítica.

---

### TAREFA 1 · Login e Acesso ao Painel Admin (Core | 2 min)
**Contexto:** O login possui botão e transição específicos ("Acessar Painel" + Dissolve) para diferenciar do ambiente das alunas. Cai direto no Dashboard.
**Roteiro:** *"Você é a gestora do Meninas Digitais e precisa acessar o painel de administração do Rede Delas. Os dados de acesso já estão preenchidos. Entre no painel."*
**Caminho:** `Tela 01 Login (versão Admin)` → `Campos pré-preenchidos` → `Acessar Painel` → `Tela 34 Dashboard Admin` ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Acessou o Dashboard sem ajuda.<br>**⚠️ Parcial:** Hesitou no botão ou tentou fluxo de aluna.<br>**❌ Falhou:** Não conseguiu acessar. | - [ ] Comentou sobre as cores ou visual do painel?<br>- [ ] Tempo até o Dashboard: ___ segundos |
> *Nota: A diferença visual previne erros. Comentários sobre isso validam o design.*

---

### TAREFA 2 · Dashboard — Leitura e Navegação (Dashboard | 2 min)
**Contexto:** Tarefa de observação pura (IHC). Avaliar se a admin compreende os KPIs e alertas de gestão (Lei de Miller).
**Roteiro:** *"Não precisa clicar em nada ainda. Olhe com atenção para essa tela e me diga em voz alta: o que essas informações estão te dizendo? O que está chamando sua atenção?"*
**Caminho:** `Tela 34 Dashboard` → Scroll vertical → Observa KPIs e Ações Pendentes ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Verbalizou métricas e pendências.<br>**⚠️ Parcial:** Citou só métricas ou só pendências.<br>**❌ Falhou:** Não inferiu informações úteis. | - [ ] Mencionou os KPIs espontaneamente?<br>- [ ] Identificou os alertas de pendência?<br>- [ ] Ordem de menção: 1º _____ 2º _____ 3º _____ |

---

### TAREFA 3 · Ativar Ada Lovelace e Excluir Perfil (Inspiradoras | 6 min)
**Contexto:** Teste do CRUD com pesos diferentes. Ativar é reversível; excluir exige confirmação de irreversibilidade.
**Roteiro 1 (Ativar):** *"No painel, há o perfil da Ada Lovelace que está inativo. Encontre e publique ele para as alunas."*
**Roteiro 2 (Excluir):** *"Agora remova permanentemente o perfil da Camila Santos (Oculta)."*
**Caminho:** `TabBar Inspiram` → `Aba Inativas` → `Card Ada` → `Lápis (Editar)` → `Ativa Toggle` → `Salvar` ✅ → `Tela 35` → `Card Camila` → `Lixeira` → `Confirmar` ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Ativou Ada e excluiu Camila c/ alerta.<br>**⚠️ Parcial:** Fez só um dos dois fluxos.<br>**❌ Falhou:** Não achou a aba "Inativas". | - [ ] Achou a aba "Inativas" sem instrução?<br>- [ ] Entendeu o toggle "Publicar agora?"?<br>- [ ] Hesitou na lixeira? Leu o aviso? (___ seg) |

---

### TAREFA 4 · Cadastrar Evento como Rascunho (Eventos | 5 min)
**Contexto:** Validação de segurança. Salvar sem publicar garante que o toggle default (desativado) protege a gestora.
**Roteiro:** *"Cadastre uma roda de conversa sobre saúde mental como rascunho — sem publicar para as alunas ainda."*
**Caminho:** `TabBar Eventos` → `FAB (+)` → `Criar Evento (Pré-preenchido)` → `Confirma Toggle Desativado` → `Salvar` → `Chip "Rascunho" na Lista` ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Cadastrou com toggle off (Rascunho).<br>**⚠️ Parcial:** Cadastrou mas publicou (ativou toggle).<br>**❌ Falhou:** Não achou o FAB (+) para criar. | - [ ] Achou o FAB (+) sozinho?<br>- [ ] Verificou o toggle antes de salvar?<br>- [ ] Viu o chip "Rascunho" aparecer na lista? |

---

### TAREFA 5 · Moderação Ética: Excluir e Ignorar (Moderação | 6 min)
**Contexto:** Maior peso ético do teste. Exige leitura de dossiê para tomar decisões opostas (ataque vs desabafo).
**Roteiro 1:** *"No painel, há dois posts denunciados. Avalie e tome a decisão no que aguarda há mais tempo (Tamires)."*
**Roteiro 2:** *"Ainda há outro post. Verifique-o (Anônima)."*
**Caminho:** `TabBar Moderação` → `Card Tamires (Detalhes)` → `Lê` → `Excluir Postagem (Vermelho)` → `Confirmar` ✅ → `Volta` → `Card Anônima (Detalhes)` → `Lê` → `Ignorar Denúncia (Âmbar)` → `Confirmar` ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Leu Detalhes e tomou decisões corretas.<br>**⚠️ Parcial:** Agiu direto da lista (sem ler contexto).<br>**❌ Falhou:** Não achou o painel de moderação. | - [ ] Abriu os Detalhes ou agiu direto da lista?<br>- [ ] Percebeu a diferença de contexto ético?<br>- [ ] Notou a cor (Vermelho x Âmbar) dos botões? |

---

### TAREFA 6 · Sanções: Enviar Aviso e Suspender (Usuárias | 5 min)
**Contexto:** Escalada de sanções (progressividade). Aviso é brando; suspensão é grave e tem feedback visual imedito.
**Roteiro 1 (Aviso):** *"A Thamires teve comportamento inadequado 1 vez. Envie um aviso educativo para o perfil dela."*
**Roteiro 2 (Suspender):** *"Agora vamos suspender a Beatriz Lopes, que possui histórico grave. Encontre e suspenda."*
**Caminho:** `TabBar Usuárias` → `Card Thamires (Detalhes)` → `Enviar Aviso (Outline)` → `Confirmar` ✅ → `Voltar` → `Card Beatriz (Detalhes)` → `Suspender Acesso (Vermelho)` → `Confirmar` → `Tag muda p/ Suspensa` ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Enviou aviso e suspendeu com sucesso.<br>**⚠️ Parcial:** Concluiu apenas uma das sanções.<br>**❌ Falhou:** Não executou as ações. | - [ ] Identificou os status visuais na lista?<br>- [ ] Leu o dossiê antes de punir?<br>- [ ] Notou a tag de status ficar vermelha? |

---

### TAREFA 7 · Retorno e Logout (Dashboard | 3 min)
**Contexto:** Encerramento via ícone global no header, testando navegabilidade cruzada.
**Roteiro:** *"Você resolveu todas as pendências! Retorne ao painel geral (Dashboard) e encerre a sua sessão de forma segura."*
**Caminho:** `Volta ao Dashboard (Via TabBar)` → `Toca no ícone Sign-Out (Header)` → `Tela 01 Login` ✅

| Critério de Sucesso | O que Observar e Anotar |
| :--- | :--- |
| **✅ Concluída:** Voltou à home e achou ícone de sair.<br>**⚠️ Parcial:** Precisou de dica para o ícone.<br>**❌ Falhou:** Não conseguiu encerrar a sessão. | - [ ] Usou a TabBar para voltar rápido?<br>- [ ] Achou o ícone de logout de primeira?<br>- [ ] Hesitou antes de sair? |

---

### EXTRA · Exploração Livre pós-Logout (2 a 3 min)
**Contexto:** Validação de desejos e necessidades da gestora (Feature Request implícito).
**Roteiro:** *"Teste finalizado! Vou te dar 2 minutinhos na tela de login. Entre e explore livremente, só pense alto."*

* **O que registrar:**
  - 1º Módulo visitado: _____________ | 2º Módulo: _____________ | 3º Módulo: _____________
  - *Comentou sobre algo que faltaria no painel administrativo? Alguma frustração?*