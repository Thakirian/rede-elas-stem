# 📱 Documentação de Teste de Usabilidade 03 — Fluxo Admin (Gestão)

**Métricas globais:** duração prevista ~38 min | Google Meet (gravação de tela e voz)
**Foco metodológico:** gestão de conteúdo, moderação, governança e tomada de decisão crítica.
**Convenção:** as telas são identificadas pelo nome.

---

### TAREFA 1 · Login e acesso ao painel (Core | 2 min)
**Contexto:** o login do painel tem botão e transição específicos ("Acessar Painel" e dissolve) para diferenciar do ambiente das alunas, e leva direto ao Dashboard.
**Roteiro:** *"Você precisa acessar o painel de administração do Rede Delas. Os dados de acesso já estão preenchidos. Entre no painel."*
**Caminho:** `Login (versão Admin)` → `Campos preenchidos` → `Acessar painel` → `Dashboard` ✅

| Critério de sucesso | O que observar e anotar |
| :--- | :--- |
| **✅ Concluída:** acessou o Dashboard sem ajuda.<br>**⚠️ Parcial:** hesitou no botão ou tentou o fluxo de aluna.<br>**❌ Falhou:** não conseguiu acessar. | - [ ] Comentou as cores ou o visual do painel?<br>- [ ] Tempo até o Dashboard: ___ s |

> *Nota: a diferença visual busca prevenir erros; comentários sobre ela são relevantes.*

---

### TAREFA 2 · Dashboard: leitura e interpretação (Dashboard | 2 min)
**Contexto:** observação pura. Avaliar se a gestora compreende as métricas e os alertas.
**Roteiro:** *"Não precisa clicar em nada ainda. Olhe com atenção para essa tela e me diga: o que essas informações estão te dizendo? O que chama sua atenção?"*
**Caminho:** `Dashboard` → rolagem vertical → leitura das métricas e das ações pendentes ✅

| Critério de sucesso | O que observar e anotar |
| :--- | :--- |
| **✅ Concluída:** verbalizou métricas e pendências.<br>**⚠️ Parcial:** citou só métricas ou só pendências.<br>**❌ Falhou:** não inferiu informações úteis. | - [ ] Mencionou as métricas espontaneamente?<br>- [ ] Identificou os alertas de pendência?<br>- [ ] Ordem: 1º ___ 2º ___ 3º ___ |

---

### TAREFA 3 · Publicar a Ada Lovelace e excluir a Camila Santos (Inspiradoras | 6 min)
**Contexto:** gestão de conteúdo com pesos diferentes. Publicar é reversível; excluir exige confirmação.
**Roteiro 1:** *"Há um perfil da Ada Lovelace inativo. Encontre-o e publique para as alunas."*
**Roteiro 2:** *"Agora remova permanentemente o perfil da Camila Santos."*
**Caminho:** `Barra inferior: Inspiram` → `Inativas` → `Ada` → `Editar` → `Ativar publicação` → `Salvar` ✅ → `Lista` → `Campos da Camila` → `Lixeira` → `Confirmar` ✅

| Critério de sucesso | O que observar e anotar |
| :--- | :--- |
| **✅ Concluída:** publicou a Ada e excluiu a Camila com a confirmação.<br>**⚠️ Parcial:** fez só um dos fluxos.<br>**❌ Falhou:** não achou os inativos. | - [ ] Achou a aba de inativas sem instrução?<br>- [ ] Entendeu a chave "Publicar agora?"<br>- [ ] Hesitou na lixeira? Leu o aviso? (___ s) |

---

### TAREFA 4 · Cadastrar evento como rascunho (Eventos | 5 min)
**Contexto:** salvar sem publicar. A chave de publicação desativada protege a gestora.
**Roteiro:** *"Cadastre uma roda de conversa sobre saúde mental como rascunho, sem publicar para as alunas ainda."*
**Caminho:** `Barra inferior: Eventos` → `Botão (+)` → `Criar evento (preenchido)` → `Confirma publicação desativada` → `Salvar` → `Chip "Rascunho" na lista` ✅

| Critério de sucesso | O que observar e anotar |
| :--- | :--- |
| **✅ Concluída:** cadastrou como rascunho.<br>**⚠️ Parcial:** cadastrou, mas publicou.<br>**❌ Falhou:** não achou o botão (+). | - [ ] Achou o botão (+) sozinha?<br>- [ ] Verificou a chave antes de salvar?<br>- [ ] Viu o chip "Rascunho" na lista? |

---

### TAREFA 5 · Moderação: excluir e ignorar (Moderação | 6 min)
**Contexto:** maior peso ético do teste. Exige leitura do contexto para decisões opostas (ataque a uma professora e desabafo).
**Roteiro 1:** *"Há dois posts denunciados. Avalie e decida sobre o que aguarda há mais tempo (Tamires)."*
**Roteiro 2:** *"Ainda há outro post. Verifique-o (Usuária Anônima)."*
**Caminho:** `Barra inferior: Moderação` → `Tamires (detalhes)` → leitura → `Excluir postagem (vermelho)` → `Confirmar` ✅ → `Voltar` → `Usuária Anônima (detalhes)` → leitura → `Ignorar denúncia` ✅

| Critério de sucesso | O que observar e anotar |
| :--- | :--- |
| **✅ Concluída:** leu os detalhes e decidiu.<br>**⚠️ Parcial:** agiu direto da lista, sem ler o contexto.<br>**❌ Falhou:** não achou a moderação. | - [ ] Abriu os detalhes ou agiu direto da lista?<br>- [ ] Percebeu a diferença de contexto entre os posts?<br>- [ ] Notou as cores dos botões? |

---

### TAREFA 6 · Aviso e suspensão (Usuárias | 5 min)
**Contexto:** sanções progressivas. O aviso é brando; a suspensão é grave e tem retorno visual imediato.
**Roteiro 1 (aviso):** *"A Tamires teve comportamento inadequado pela primeira vez. Envie um aviso educativo ao perfil dela."*
**Roteiro 2 (suspensão):** *"Agora vamos suspender o acesso da Bárbara Lopes, que tem histórico grave. Encontre o perfil e tome a decisão."*
**Caminho:** `Barra inferior: Usuárias` → `Tamires (detalhes)` → `Enviar aviso` → `Confirmar` ✅ → `Voltar` → `Bárbara Lopes (detalhes)` → `Suspender acesso (vermelho)` → `Confirmar` → `Etiqueta muda para "Suspensa"` ✅

| Critério de sucesso | O que observar e anotar |
| :--- | :--- |
| **✅ Concluída:** enviou o aviso e suspendeu.<br>**⚠️ Parcial:** concluiu só uma das sanções.<br>**❌ Falhou:** não executou as ações. | - [ ] Identificou os status na lista?<br>- [ ] Leu o histórico de conduta antes de decidir?<br>- [ ] Notou a etiqueta ficar vermelha? |

---

### TAREFA 7 · Retorno ao Dashboard e logout (Dashboard | 3 min)
**Contexto:** encerramento pelo ícone de sair do cabeçalho; testa a navegação entre áreas.
**Roteiro:** *"Você resolveu todas as pendências. Retorne ao painel geral (Dashboard) e encerre a sua sessão de forma segura."*
**Caminho:** `Barra inferior: Dashboard` → `Ícone de sair (cabeçalho)` → `Login` ✅

| Critério de sucesso | O que observar e anotar |
| :--- | :--- |
| **✅ Concluída:** voltou ao Dashboard e achou o ícone de sair.<br>**⚠️ Parcial:** precisou de dica para o ícone.<br>**❌ Falhou:** não encerrou a sessão. | - [ ] Usou a barra inferior para voltar?<br>- [ ] Achou o ícone de sair de primeira?<br>- [ ] Hesitou antes de sair? |

---

### EXTRA · Exploração livre (2 a 3 min)
**Roteiro:** *"O teste oficial acabou. Vou te dar alguns minutos para explorar o painel livremente, só continue pensando alto."*

- **O que registrar:** 
  - 1º, 2º e 3º módulo visitado.
  - Algo que faltaria no painel.
  - Frustrações.