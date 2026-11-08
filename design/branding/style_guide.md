# 🎨 Guia de Estilo: Rede Delas

Este documento resume o sistema de *design* aplicado ao protótipo avaliado (v1.0). O arquivo *Figma Style Guide* desta pasta traz a prancha visual correspondente.

## 1. Paleta de Cores

Os tons frios (roxo e turquesa) transmitem profissionalismo e inovação, e os tons quentes (rosa e lilás) transmitem empatia. O roxo primário é a cor de identidade e de ação (botões, ícones ativos e cabeçalhos), o rosa reforça o acolhimento e, em tom mais forte, as ações de recusa e de denúncia, e o turquesa e o verde indicam categorias, disciplinas e estados de sucesso. O painel administrativo adota cabeçalho e barra de navegação em roxo escuro e fundo lavanda, o que o distingue visualmente da versão das usuárias.

| Grupo | Nome | Valor (Hex) | Uso principal |
| :--- | :--- | :--- | :--- |
| **Marca** | Roxo primário | `#6C4CF1` | Botões primários, ícones ativos, cabeçalhos |
| **Marca** | Roxo escuro | `#4B2FBF` | Contraste e profundidade; identidade da Admin |
| **Marca** | Noite STEM | `#2D1B6E` | Títulos; cabeçalho e barra do painel administrativo |
| **Marca** | Roxo claro | `#A99BFF` | Ícones inativos |
| **Marca** | Lilás suave | `#EDE9FB` | Fundos de *chips*, item ativo da barra, superfícies |
| **Rosa** | Acolhimento | `#D4537E` | Destaques, recusa e denúncia |
| **Rosa** | Escuro, médio e suave | `#72243E`, `#ED9381`, `#FCE7F3` | Alertas graves, realces e fundos de *chips* |
| **Turquesa** | Escuro, principal e claro | `#0F6E56`, `#2EC4B6`, `#7DE2D1` | Categorias, disciplinas e sucesso |
| **Fundo** | App; telas internas e chat; cartões | `#F9F7FF`, `#F4F1FC`, `#FFFFFF` | Superfícies |
| **Borda** | Suave; cartões da Admin | `#E5E0FF`, `#D8D0F0` | Contornos |
| **Texto** | Primário; secundário | `#1E1A3C`, `#6B5E9B` | Texto corrido e de apoio |
| **Texto** | Título; discreto; dica | `#2D1B6E`, `#8B7EB8`, `#9B8AC4` | Títulos, metadados e *placeholders* |
| **Estado** | Sucesso | `#22C55E` (fundo `#DCFCE7`) | Disponível, aceito, concluído |
| **Estado** | Atenção | `#F59E0B` (fundo `#FEF3C7`) | Pendente, aguardando |
| **Estado** | Erro | `#EF4444` | Recusar, excluir, erro crítico |

## 2. Tipografia, Ícones e Parâmetros de Forma

Os títulos usam a família *Plus Jakarta Sans*, de aspecto contemporâneo e acolhedor, e o corpo de texto usa a *Inter*, de alta legibilidade em telas pequenas. Os ícones pertencem à biblioteca *Phosphor*.

### 2.1 Estilos de Texto
| Estilo | Família | Tamanho | Peso |
| :--- | :--- | :--- | :--- |
| **Título 1** | Plus Jakarta Sans | 24 px | Negrito (700) |
| **Título 2** | Plus Jakarta Sans | 20 px | Seminegrito (600) |
| **Título 3** | Plus Jakarta Sans | 16 px | Seminegrito (600) |
| **Título 4** | Plus Jakarta Sans | 13 px | Negrito (700) |
| **Corpo** | Inter | 14 px | Regular (400) e Médio (500) |
| **Corpo pequeno** | Inter | 12 px | Regular (400) |
| **Rótulo; rótulo em caixa alta**| Plus Jakarta Sans | 11 px; 10 px (espaçamento 8%)| Negrito (700) |
| **Legenda** | Inter | 11 px | Regular (400) |

### 2.2 Parâmetros de Forma, Sombra e Espaçamento
| Parâmetro | Valores |
| :--- | :--- |
| **Raio dos cantos** | 4, 8, 12, 16 e 24 px; circular para *chips*, abas e avatares |
| **Sombra de cartão** | Deslocamento vertical de 2 px, desfoque de 8 px, roxo primário a 8% |
| **Sombra de janela sobreposta** | Deslocamento vertical de 8 px, desfoque de 32 px, roxo primário a 12% |
| **Tela de referência** | 390 × 844 px (iPhone 14 Pro) |
| **Margem lateral e largura útil** | 20 px e 350 px |
| **Espaçamento entre blocos** | Múltiplos de 4, em geral 8, 12, 16 e 24 px |

## 3. Componentes

A biblioteca de componentes foi construída no Figma com *Auto Layout* e variantes de estado, de modo que cada elemento se ajusta ao conteúdo e é reutilizado nas telas.

| Família de Componentes | Variantes |
| :--- | :--- |
| **Botões** | Primário, secundário (contorno), perigo, administrador e *ghost* |
| **Campos de formulário** | Padrão, foco, erro, senha, busca, lista suspensa e área de texto |
| **Navegação** | Barra inferior da usuária (Home, Inspiram, Conexões, Eventos e Fórum), barra inferior da Admin (Dashboard, Inspiram, Eventos, Moderação e Usuárias) e cabeçalhos |
| **Identificação** | Avatar genérico, com iniciais e da Admin, em três tamanhos; indicadores de disponibilidade |
| **Seleção e estado** | *Chips* (inativo, ativo, rosa, turquesa e de atenção), chave liga-desliga e controle segmentado de duas e de três abas |
| **Cartões** | Mentora (disponível e ocupada), evento, *post* (identificado e anônimo), perfil inspirador, notificação (lida e não lida), *status* de conexão e destaque da inspiradora do dia |
| **Seções da tela inicial**| Carrossel de eventos, pílula de acolhimento e campo de postagem |
| **Chat** | Balões enviado e recebido; barra de resposta |
| **Feedback** | Estados vazios, janelas de confirmação e folhas inferiores (solicitação, avaliação e denúncia) |