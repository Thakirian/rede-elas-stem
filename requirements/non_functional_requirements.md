# ⚙️ Requisitos Não-Funcionais (RNF) - Rede Delas

Este documento define os atributos de qualidade, restrições técnicas e diretrizes que o sistema Rede Delas deve respeitar para garantir uma experiência de uso eficiente e segura.

## 1. Tabela de Requisitos

| ID | Descrição | Categoria |
| :--- | :--- | :--- |
| **RNF01** | A interface deve ser projetada especificamente para dispositivos móveis (Android/iOS). | Portabilidade |
| **RNF02** | O sistema deve possuir interface intuitiva baseada nas 10 Heurísticas de Nielsen. | Usabilidade |
| **RNF03** | O sistema deve garantir a privacidade total, desvinculando dados em posts anônimos. | Segurança |
| **RNF04** | O design deve possuir contraste e tipografia acessíveis seguindo padrões WCAG. | Acessibilidade |
| **RNF05** | O tempo de carregamento entre transições de tela no protótipo deve ser fluido (< 300ms). | Performance |

## 2. Detalhamento e Critérios de Qualidade

* **Usabilidade (RNF02):** O protótipo será avaliado através da escala SUS (System Usability Scale) com o público-alvo. O objetivo é atingir um score que classifique a usabilidade como "Boa" ou "Excelente", garantindo que calouras consigam navegar sem treinamento prévio.
* **Segurança e Privacidade (RNF03):** No módulo de Acolhimento, a funcionalidade de anonimato deve ser robusta o suficiente para que nem mesmo outras usuárias da rede consigam rastrear a autoria de um post anônimo através da interface de front-end.
* **Acessibilidade (RNF04):** Aplicação de diretrizes básicas do WCAG (Web Content Accessibility Guidelines), focando em tamanhos de fonte legíveis (mínimo 14px para corpo de texto) e taxa de contraste adequada para elementos clicáveis.
* **Portabilidade (RNF01):** O design no Figma utilizará viewports padrão de smartphones modernos, garantindo que a hierarquia de informações não seja prejudicada em telas menores.

> **Nota Metodológica:** Os requisitos de performance (RNF05) referem-se à fluidez das animações e transições configuradas no protótipo de média-fidelidade para simular o comportamento de um aplicativo nativo.