# Tasks: Expo Android APK Delivery

**Input**: Design documents from `specs/002-expo-apk-delivery/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/eas-build-contract.md, research.md

## Dependency Graph

- Phase 1 (Expo Setup) → Phase 2 (EAS Config)
- Phase 2 (EAS Config) → Phase 3 (Build Generation)
- Phase 3 (Build Generation) → Phase 4 (Hardware Validation)

## Phase 1: Expo Setup (Shared Infrastructure)

**Purpose**: Migrate the current mobile project to the Expo ecosystem.

- [X] T001 Initialize Expo SDK and install core dependencies in `mobile/package.json`
- [X] T002 [P] Create Expo entry point `mobile/AppEntry.js`
- [X] T003 [P] Configure Expo scripts (`start`, `run:android`) in `mobile/package.json`
- [X] T004 [US1] Install native module support `expo-dev-client` in `mobile/`

---

## Phase 2: EAS Configuration (Foundational)

**Purpose**: Set up the build infrastructure for APK generation.

- [X] T005 [P] Create global app configuration in `mobile/app.json` per `data-model.md`
- [X] T006 [P] Implement build profiles in `mobile/eas.json` per `contracts/eas-build-contract.md`
- [X] T007 [US1] Configure native plugins for `react-native-tcp-socket` and `camera-kit` in `mobile/app.json`
- [X] T008 Install EAS CLI globally and link project to Expo account

---

## Phase 3: Build & Artifact Generation (US2)

**Goal**: Generate the installable APK file using EAS Build.

**Independent Test**: Download and verify the generated `.apk` file.

- [ ] T009 [US2] Run `eas build:configure` to initialize Android credentials
- [ ] T010 [US2] Execute remote build command for `preview` profile (APK format)
- [ ] T011 [US2] Download the generated APK artifact from Expo dashboard
- [ ] T012 [P] [US2] Verify APK file integrity and signature

---

## Phase 4: Hardware Validation (US3)

**Goal**: Validate the application on a physical Android device.

**Independent Test**: Connect the physical app to the Host and send a media command.

- [ ] T013 [US3] Install APK on physical Android device (via Sideloading)
- [ ] T014 [US3] Perform QR Code pairing test with Host `server/`
- [ ] T015 [US3] Validate VLC Media Control commands (Play/Pause/Vol) from physical device
- [ ] T016 [US3] Measure latency and network stability on physical device

---

## Phase 5: Polish & Final Documentation

- [ ] T017 [P] Update `docs/quickstart.md` with final APK installation instructions
- [ ] T018 Cleanup temporary build files and credentials
- [ ] T019 Final code review of Expo configurations per Clean Code principles

---

## Implementation Strategy

1. **Setup First**: Complete Phase 1 and 2 to ensure the environment is ready.
2. **Build MVP**: Complete Phase 3 to get the first installable APK.
3. **Validate**: Perform Phase 4 hardware tests to confirm connectivity.

## Parallel Opportunities

- **T002, T003**: Entry point and scripts can be set up simultaneously.
- **T005, T006**: `app.json` and `eas.json` can be drafted in parallel.
- **T012**: Verification can be prepared while the build is running in the cloud.
