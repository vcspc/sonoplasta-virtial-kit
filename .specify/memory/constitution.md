<!--
Sync Impact Report:
- Version change: N/A → 1.0.0
- List of modified principles: Initial definition.
- Added sections: Core Principles, Restrições Tecnológicas, Fluxo de Desenvolvimento, Governance.
- Removed sections: None.
- Templates requiring updates:
    - ✅ .specify/templates/plan-template.md (aligned with "Constitution Check")
    - ✅ .specify/templates/spec-template.md (aligned)
    - ✅ .specify/templates/tasks-template.md (aligned)
- Follow-up TODOs: None.
-->

# sonopalsta-virtual-kit Constitution

## Core Principles

### I. Clean Code & Modularidade
O código deve ser legível, modular e seguir os princípios SOLID. Funções e classes devem ter responsabilidade única. Comentários devem explicar o "porquê" e não o "o quê", em português brasileiro, garantindo que qualquer desenvolvedor consiga manter o sistema.

### II. Documentação Proativa
Toda nova funcionalidade ou alteração arquitetural deve ser refletida na pasta `docs`. A documentação é parte integrante do código e deve estar sempre sincronizada. Se a pasta `docs` não existir, ela deve ser criada imediatamente.

### III. Testes como Requisito (NON-NEGOTIABLE)
O desenvolvimento deve ser orientado a testes (TDD). Nenhum código de produção deve ser aceito sem testes unitários e de integração que validem o comportamento esperado e evitem regressões em funcionalidades críticas de áudio e eventos.

### IV. Performance e Baixa Latência
Como um kit de sonoplastia virtual, o sistema deve garantir processamento eficiente. Algoritmos e integrações devem ser otimizados para minimizar a latência, garantindo que a resposta sonora seja imediata ao gatilho do usuário.

### V. Versionamento Semântico e Evolução Segura
Mudanças na API ou no comportamento do kit devem seguir rigorosamente o versionamento semântico (SemVer). Mudanças que quebram a compatibilidade (Breaking Changes) devem ser justificadas e acompanhadas de um plano de migração claro.

## Restrições Tecnológicas

O projeto utiliza o ecossistema Node.js com TypeScript para garantir segurança de tipos. A introdução de novas bibliotecas externas exige a consulta prévia à documentação oficial e a validação de que a biblioteca é mantida e performática.

## Fluxo de Desenvolvimento

O ciclo de vida de cada funcionalidade deve seguir o fluxo: Pesquisa -> Estratégia -> Execução (Plano, Ação, Validação). O uso de Conventional Commits é obrigatório para manter um histórico de mudanças legível e automatizável.

## Governance

Esta constituição é a autoridade máxima sobre as práticas de desenvolvimento do projeto. Qualquer divergência entre o código e estes princípios deve ser tratada como um bug crítico. Alterações nesta constituição exigem um incremento de versão e a atualização do Relatório de Impacto de Sincronização.

**Version**: 1.0.0 | **Ratified**: 2026-03-12 | **Last Amended**: 2026-03-12
