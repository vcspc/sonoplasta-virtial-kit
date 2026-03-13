# Tasks: Church Sound Assistant

**Input**: Design documents from `specs/001-church-sound-assistant/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/socket-protocol.md, research.md

## Dependency Graph

- Phase 1 (Setup) → Phase 2 (Foundational)
- Phase 2 (Foundational) → Phase 3 (US1: Core Remote)
- Phase 3 (US1) → Phase 4 (US2: YouTube Search/Download)
- Phase 3 (US1) → Phase 5 (US3: Schedule/Organization)
- Phase 2 (Foundational) → Phase 6 (US4: Communication/Overlay)

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization for both Host (Python) and Client (React Native).

- [X] T001 Initialize Python environment and directory structure in `server/`
- [X] T002 [P] Create `server/requirements.txt` with dependencies (pyautogui, yt-dlp, qrcode, pillow)
- [X] T003 [P] Initialize React Native project in `mobile/`
- [X] T004 [P] Install mobile dependencies (`react-native-tcp-socket`, `react-native-camera-kit`)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core communication layer (TCP Sockets) required for all features.

- [X] T005 Implement base TCP Server with multi-client support in `server/core/socket_server.py`
- [X] T006 [P] Implement base TCP Client service in `mobile/src/services/socket_client.ts`
- [X] T007 [P] Create JSON command parser/validator per `contracts/socket-protocol.md` in `server/core/protocol.py`
- [X] T008 [P] Configure global error handling and logging in `server/core/logger.py`

**Checkpoint**: Socket communication established between Python and React Native.

---

## Phase 3: User Story 1 - Conexão e Controle Remoto (Priority: P1) 🎯 MVP

**Goal**: QR Code pairing and basic VLC media control.

**Independent Test**: Scan QR Code from mobile and toggle VLC Play/Pause on PC.

- [X] T009 [US1] Implement IP discovery and QR Code generator in `server/core/discovery.py`
- [X] T010 [P] [US1] Create QR Code scanner screen in `mobile/src/navigation/ConnectScreen.tsx`
- [X] T011 [US1] Implement VLC Controller using `pyautogui` and HTTP in `server/core/controller.py`
- [X] T012 [P] [US1] Create Media Control UI (Play/Pause, Vol, Fullscreen) in `mobile/src/components/MediaControls.tsx`
- [X] T013 [US1] Map socket commands to `VLCController` actions in `server/main.py`

**Checkpoint**: Core remote control (MVP) functional.

---

## Phase 4: User Story 2 - Projeção e Download YouTube (Priority: P2)

**Goal**: Search YouTube on mobile and play/download on Host.

**Independent Test**: Search for a video, click play, and verify it opens in Host's browser in fullscreen.

- [X] T014 [US2] Implement YouTube Search service using `yt-dlp` or API in `server/core/youtube.py`
- [X] T015 [P] [US2] Create Search UI with results list in `mobile/src/components/YoutubeSearch.tsx`
- [X] T016 [US2] Implement `YT_DOWNLOAD` logic (Audio/Video) in `server/core/youtube.py`
- [X] T017 [P] [US2] Add download trigger buttons to search results in `mobile/src/components/SearchResultItem.tsx`
- [X] T018 [US2] Implement browser automation for fullscreen YouTube playback in `server/core/controller.py`

---

## Phase 5: User Story 3 - Organização e Cronograma (Priority: P2)

**Goal**: Manage a sequence of local files and links.

- [X] T019 [US3] Create Local File Search service in `server/core/file_system.py`
- [X] T020 [P] [US3] Create Schedule Model and Persistence (JSON) in `server/core/schedule.py`
- [X] T021 [P] [US3] Implement Schedule UI with drag-and-drop reordering in `mobile/src/navigation/ScheduleScreen.tsx`
- [X] T022 [US3] Implement remote file opening command in `server/core/controller.py`

---

## Phase 6: User Story 4 - Comunicação e Monitoramento (Priority: P3)

**Goal**: Real-time chat and Host UI overlay.

- [X] T023 [US4] Create Overlay UI (QR Code, Chat, Logs) using `tkinter` or `PyQt` in `server/main.py`
- [X] T024 [P] [US4] Implement Chat UI and Message history in `mobile/src/components/ChatComponent.tsx`
- [X] T025 [US4] Implement Host notification system for incoming messages in `server/core/notifications.py`
- [X] T026 [P] [US4] Implement File Transfer with Password Auth in `server/core/socket_server.py`

---

## Phase 7: Polish & Cross-Cutting Concerns

- [X] T027 [P] Implement password-protected file transfer UI in `mobile/src/components/FileTransfer.tsx`
- [X] T028 Performance optimization: Ensure latency < 200ms
- [X] T029 Final validation of `docs/quickstart.md`
- [X] T030 Final code review and cleanup per Clean Code principles

---

## Implementation Strategy

1. **MVP First**: Complete Phases 1, 2, and 3. This delivers the core value (Remote VLC Control).
2. **Incremental**: Add YouTube search/playback (Phase 4), then organizational tools (Phase 5).
3. **Advanced**: Finish with communication and overlay (Phase 6).

## Parallel Opportunities

- **T002, T003, T004**: Infrastructure setup can happen simultaneously.
- **T010, T012**: Mobile UI development can run in parallel with Host controller logic.
- **T015, T017, T021**: Mobile feature UIs can be developed in parallel once Phase 2 is done.
