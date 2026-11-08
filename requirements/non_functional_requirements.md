# ⚙️ Requisitos Não-Funcionais (RNF) - Rede Delas

Este documento define os atributos de qualidade, restrições técnicas e diretrizes que o sistema Rede Delas deve respeitar para garantir uma experiência de uso eficiente e segura.

## 1. Tabela de Requisitos

| ID | Descrição | Categoria |
| :--- | :--- | :--- |
| **RNF01** | A interface deve ser projetada para dispositivos móveis (Android e iOS). | Portabilidade |
| **RNF02** | A interface deve ser intuitiva, orientada pelas 10 heurísticas de Nielsen. | Usabilidade |
| **RNF03** | A privacidade deve ser garantida nas postagens anônimas, com a identidade da autora desvinculada da exibição pública. | Segurança |
| **RNF04** | O design deve buscar contraste e tipografia legíveis, tomando como referência as diretrizes de acessibilidade WCAG. | Acessibilidade |
| **RNF05** | As transições entre telas devem ser fluidas, com animação padronizada de 300 ms. | Desempenho |

## 2. Detalhamento e Critérios de Qualidade

- **Portabilidade (RNF01):** o design no Figma usa como referência a tela de 390 × 844 px (iPhone 14 Pro), de modo que a hierarquia de informações se mantenha em smartphones modernos.
- **Usabilidade (RNF02):** o protótipo é avaliado por testes de usabilidade com a técnica *Thinking Aloud* e pela escala SUS (*System Usability Scale*) com o público-alvo (ver results/). O objetivo é que usuárias novas consigam navegar sem treinamento prévio.
- **Segurança e privacidade (RNF03):** no módulo de Acolhimento, a autoria de um post anônimo não deve ser rastreável pela interface. No protótipo, a proteção é representada visualmente (a chave de anonimato troca nome e foto por um avatar genérico antes da publicação); a desvinculação efetiva dos dados é uma exigência para uma futura implementação.
- **Acessibilidade (RNF04):** as diretrizes WCAG foram adotadas como referência de projeto. Não houve auditoria formal de acessibilidade.
- **Desempenho (RNF05):** refere-se à fluidez das animações e transições configuradas no protótipo (*Smart Animate* de 300 ms), e não a uma medição de desempenho de software.

> **Nota Metodológica:** os requisitos acima foram verificados no protótipo interativo de alta fidelidade com fluxo guiado, e não em um sistema implementado.