# 경력기술서

> 1~3년차 MES 백엔드 개발자 | Spring Boot · PostgreSQL · SAP ERP 연동

---

## 핵심 요약

- Spring Boot 기반 **제조실행시스템(MES) 백엔드 단독 설계 및 운영** (Java 518파일, REST API 400+)
- 자재·생산·설비·품질·출하 전 도메인 커버, **PostgreSQL 프로시저 42종 / 함수 15종** 직접 작성
- **RSA-2048 + AES-256 이중 암호화** 인증 구조 설계 및 SAP ERP RFC 연동 구현
- **커스텀 RBAC 권한 체계** 독자 설계 (Spring Security 미사용, URL 단위 CRUD 제어)
- SVN 최근 리비전 r33,462 — 장기 운영 기간의 실질적 기여 이력

---

## 경력

### 현대위아 MES 시스템 개발·운영 | 백엔드 개발자

**담당 역할:** Spring Boot REST API 백엔드 개발, PostgreSQL 프로시저·함수 설계, ERP 인터페이스 구현, 권한·보안 체계 구축

---

## 주요 성과

### 1. 권한 및 보안 체계 구축

> **Spring Security 없이** 커스텀 인터셉터 기반 인증·인가 파이프라인 독자 설계

- `ApiInterceptor` — 모든 API 요청에 세션 유효성, 역할코드, URL CRUD 권한을 순차 검증
- URL 단위 CRUD(GET/POST/PUT/DELETE) 권한을 DB에 저장, 인메모리 캐시(`AuthorizationCache`)로 운영 중 성능 보장
- Longest-prefix 매칭 방식으로 URL 트리 전체를 단일 패턴으로 커버
- `ApiEndpointScanner` — 서버 기동 시 전체 엔드포인트를 자동 수집해 `ma_url_permission` 테이블에 등록 (PENDING → ACTIVE 단계 관리)
- 관리자 API(`/Auth/reloadPermission`)로 **서버 재시작 없이 권한 캐시 즉시 반영**

**성과 문장:**
> UI 중심 권한 체크 구조를 HTTP 메서드 단위 API 레벨 검증 방식으로 재설계해 운영 시스템 접근 통제를 강화했다.

---

### 2. 이중 암호화 인증 + SSO 연동

> RSA-2048 / AES-256 / 기업 SSO 3개 인증 경로 통합 구현

- **RSA-2048 OAEP** — 클라이언트가 서버 공개키로 비밀번호 암호화, 서버에서 개인키 복호화 (`GET /Auth/publicKey` → `POST /Auth`)
- **AES-256 세션 암호화** — 모바일·PDA 채널의 암호화 페이로드 처리 (`sessionAesKey`)
- **NETS SSO** — 기업 포털 Single Sign-On 연동 (`/Auth/SSO`)
- 로그인 실패 10회 → 24시간 계정 잠금, 관리자 IP 화이트리스트 적용
- Jasypt를 통한 `application.properties` DB 자격증명 암호화 (`ENC(...)`)

**성과 문장:**
> 다중 암호화 인증(RSA-2048 전송 암호화, AES-256 세션 암호화) 및 엔터프라이즈 SSO 연동 구조를 구현해 운영 시스템 보안성을 높였다.

---

### 3. 개인정보 비식별화 이중 적용

> DB 레이어와 API 레이어 양쪽에서 마스킹 처리

- **DB 함수** `fn_mask_pers_info` — 쿼리 시점에 PII 마스킹 적용
- **Java 유틸** `DataMaskingUtil` — 이름(첫 글자), 전화번호(뒤 4자리), 이메일(로컬파트), 주소(10자), 우편번호, 팩스를 API 응답에서 마스킹
- 출하 관리 차량 조회 등 현업 노출 화면에 일괄 적용

**성과 문장:**
> DB 함수 및 Java API 레이어 이중 마스킹 정책을 수립·적용해 실운영 환경의 개인정보 보호 준수 수준을 높였다.

---

### 4. PostgreSQL 프로시저·함수 42 + 15종 설계

> 자재·생산·설비·출하 핵심 트랜잭션을 프로시저로 처리

**자재 도메인 (Material)**

| 프로시저 | 기능 |
|---|---|
| `sp_set_stock_po` | PO 기반 자재 입고 처리 |
| `sp_set_stock_npo` | Non-PO 자재 입고 처리 |
| `sp_set_stock_mtl_rcv` | 일반 자재 수령 |
| `sp_set_mat_stock_new` | LOT 번호 자동 채번 + 신규 재고 생성 |
| `sp_set_mat_stock_split` | 재고 LOT 분할 |
| `sp_set_mat_stock_merge` | 재고 LOT 합치기 |
| `sp_set_mat_adjust` | 재고 조정 처리 |
| `sp_set_mat_out` | 자재 출고 처리 |
| `sp_set_stock_cncl` | 재고 트랜잭션 취소 |

**생산 도메인 (Production)**

| 프로시저 | 기능 |
|---|---|
| `sp_set_hi_prod_result` | 생산실적 등록 (계획 조회, BOM, 바코드, 파렛 연동) |
| `sp_set_wip_result` | 공정 작업 실적 등록 |
| `sp_set_final_process` | 최종 공정 결과 등록 |
| `sp_set_finish_result` | 완성품 결과 등록 |
| `sp_st_prod_process_result` | 공정별 생산실적 집계 |
| `sp_st_prod_process_result_hour` | 시간대별 공정 실적 집계 |

**설비 도메인 (Equipment)**

| 프로시저/트리거 | 기능 |
|---|---|
| `sp_set_main_result` | 사후보전 결과 등록 |
| `sp_set_main_prevent_result` | 예방보전 결과 등록 |
| `trg_main_call_occur` | 설비 알람 발생 시 카카오톡 알림 자동 발송 트리거 |

**ERP 인터페이스 도메인**

| 프로시저 | 기능 |
|---|---|
| `sp_set_if_mat_in_npo_cncl_result` | ERP NPO 입고 취소 결과 반영 |
| `sp_set_if_mm_send_mat_in_npo_cncl` | ERP로 NPO 취소 전송 |

**함수 (Functions)**

| 함수 | 기능 |
|---|---|
| `fn_mask_pers_info` | 개인정보 마스킹 (DB 레이어) |
| `fn_set_stock_qty` | 자재 재고 수량 갱신 |
| `fn_set_main_stock_qty` | 설비 부품 재고 수량 갱신 |
| `fn_tbl_prod_plan` | 생산계획 집합 반환 함수 |
| `fn_tbl_pallet_load_lot_list` | 파렛 적재 LOT 목록 반환 |
| `fn_get_work_date` | 교대 규칙 기반 작업일 계산 |
| `fn_tbl_customer_master_list` | 고객사 마스터 페이징 반환 |
| `fn_tbl_vend_master_list` | 협력사 마스터 페이징 반환 |
| `fn_tbl_serial_search` | 바코드/시리얼 검색 |
| `fn_tbl_user_list` | 사용자 목록 페이징 반환 |

**성과 문장:**
> 재고 LOT 채번·분할·합치기, 생산실적 등록, ERP 인터페이스 취소 등 핵심 트랜잭션을 PostgreSQL 프로시저로 설계해 데이터 정합성과 유지보수성을 높였다.

---

### 5. SAP ERP RFC 연동 (Spring WebClient)

> MES ↔ SAP ERP 자재 이동 9개 트랜잭션 연동

- Spring WebClient (Reactive) 기반 RFC 어댑터 호출
- 어댑터 통신 실패 시 `RuntimeException` throw → MES DB 트랜잭션 자동 롤백
- 지원 시나리오: 무상공급, 자재출고, PO/NPO/수입/일반 입고, 반납, 유상판매, 입하확인

**성과 문장:**
> Spring WebClient를 활용해 SAP ERP RFC 어댑터와 9종 자재 이동 트랜잭션을 연동하고, 통신 실패 시 MES 트랜잭션 롤백 구조를 구현했다.

---

### 6. 이중 DB 구성 (PostgreSQL + MSSQL)

> 도메인별 데이터베이스 분리, 단일 애플리케이션 내 이중 DataSource 운영

- **PostgreSQL** — MES 전체 업무 데이터 (Primary)
- **MSSQL** — SPC·품질 데이터 별도 서버 연동 (Secondary)
- HikariCP 커넥션 풀, MyBatis, `@Primary` / `@Qualifier` 분리 구성
- X-Bar/R 관리도 계산 로직 Java 서버 구현

**성과 문장:**
> 이중 DataSource(PostgreSQL + SQL Server) 구성과 HikariCP 커넥션 풀을 운영해 도메인 분리 DB 환경에서 안정적인 데이터 조회를 지원했다.

---

### 7. 모바일 PDA 전용 API 설계 (55+ 엔드포인트)

> 창고 작업자 바코드 스캐너 워크플로우 전용 API 구현

- 카트 조회·등록·변경·적재·초기화
- 파렛 적재, 시리얼/바코드 검색
- 자재 입고(파트너/무파트너), 자재 출고·이동·현장재고
- 불량품 반품, 초과입력 반납
- 출하계획 조회, 예약/유상/무상 출고

**성과 문장:**
> 창고 PDA 단말 전용 모바일 API 55종을 설계·구현해 바코드 스캐너 기반 현장 업무 디지털화를 지원했다.

---

### 8. 설비 알람 → 카카오톡 자동 알림

- PostgreSQL 트리거 `trg_main_call_occur` — 설비 알람 발생 즉시 `ITA_TALK_TRAN` 테이블에 발송 레코드 생성
- 카카오 비즈메시지 연동 서비스가 해당 레코드를 소비해 담당자에게 푸시 알림
- 알람 코드·템플릿·수신자 정보 자동 매핑

**성과 문장:**
> DB 트리거 기반 카카오 비즈메시지 자동 알림 구조를 구현해 설비 이상 발생 시 담당자 즉시 대응 체계를 갖췄다.

---

## 기술 스택

| 분류 | 기술 |
|---|---|
| Language | Java 17 |
| Framework | Spring Boot, Spring WebClient (Reactive) |
| ORM | MyBatis |
| DB | PostgreSQL (Primary), Microsoft SQL Server (Secondary) |
| Connection Pool | HikariCP |
| 보안 | RSA-2048 OAEP, AES-256 CBC, Jasypt, NETS SSO |
| 보고서 | JasperReports (PDF 출하 증명서) |
| 통계 | SPC X-Bar/R 관리도 (Java 직접 구현) |
| 알림 | 카카오 비즈메시지 (DB 트리거 연동) |
| ERP | SAP RFC (Spring WebClient 어댑터) |
| 버전관리 | SVN (최근 리비전 r33,462) |
| 배포 환경 | Tomcat, Windows Server |

---

## 시스템 규모

| 항목 | 수치 |
|---|---|
| Java 소스 파일 | 518개 |
| REST API 엔드포인트 | 400개 이상 |
| SQL 프로시저 | 42종 |
| SQL 함수 | 15종 |
| SQL 테이블 DDL | 7종 |
| DB 트리거 | 1종 |
| 도메인 엔티티 클래스 | 약 90개 |
| 커버 도메인 | 생산·자재·설비·품질·출하·시스템·모바일 |
| SVN 최근 리비전 | r33,462 |

---

## 이력서 문장 모음 (복붙용)

```
• Spring Boot 기반 MES 백엔드를 단독 설계·운영하며 생산·자재·설비·품질·출하 7개 도메인, 
  REST API 400종 이상을 구현했다.

• RSA-2048 전송 암호화 + AES-256 세션 암호화 이중 인증 구조와 기업 SSO(NETS) 연동을 
  구현해 운영 시스템 보안성을 강화했다.

• Spring Security 없이 커스텀 인터셉터 기반 RBAC 권한 체계를 설계하고 URL 단위 
  CRUD 권한 캐시와 자동 엔드포인트 탐지 기능을 구현해 운영 중 무중단 권한 관리를 실현했다.

• PostgreSQL 저장 프로시저 42종·함수 15종을 직접 설계해 재고 LOT 채번·분할·합치기, 
  생산실적 등록, ERP 인터페이스 취소 등 핵심 트랜잭션의 정합성을 확보했다.

• Spring WebClient로 SAP ERP RFC 어댑터와 9종 자재 이동 트랜잭션을 연동하고 
  통신 실패 시 MES 트랜잭션 롤백 구조를 구현했다.

• DB 함수(fn_mask_pers_info)와 Java API 레이어 이중 마스킹 정책을 수립·적용해 
  실운영 환경의 개인정보 보호 기준을 충족했다.

• PostgreSQL 트리거 기반 카카오 비즈메시지 자동 알림 구조로 설비 이상 발생 시 
  담당자 즉시 대응 체계를 구현했다.

• PDA 바코드 스캐너 전용 모바일 API 55종을 설계해 창고 현장 업무 디지털화를 지원했다.
```
