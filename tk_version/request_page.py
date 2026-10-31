"""صفحه ثبت و مشاهده درخواست‌های تعمیرات (tblkar) در نسخه Tkinter."""
from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk

import jdatetime

from db_config import get_connection
from .rtl import rtl_text
from .theme import COLORS


UNIT_NAMES = {
    "tamerat": "تعمیرات عمومی",
    "kala": "عملیات کالا",
    "khadamat": "خدمات اداری و اجتماعی",
    "hse": "ایمنی",
    "harasat": "حراست",
}

CORE_COLUMNS = (
    "wonumber", "vahed", "tarikhdarkhast", "mozooe",
    "mahalkarf", "mahalkara", "sharh", "darkhastkonande",
)


def _normalize_digits(value: object) -> str:
    table = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789")
    return str(value or "").translate(table)


def _display_date(value: object) -> str:
    if value in (None, ""):
        return ""
    text = _normalize_digits(value).strip()
    digits = "".join(ch for ch in text if ch.isdigit())
    if len(digits) == 8:
        return f"{digits[:4]}/{digits[4:6]}/{digits[6:8]}"
    return text


def _unit_name(value: object) -> str:
    raw = str(value or "").strip()
    return UNIT_NAMES.get(raw.casefold(), raw)


class RequestPage(ttk.Frame):
    """فرم ثبت درخواست + جدول مشاهده، جست‌وجو و فیلتر درخواست‌ها."""

    def __init__(self, master, current_user: dict):
        super().__init__(master, style="Surface.TFrame", padding=16)
        self.current_user = current_user or {}
        self.username = str(
            self.current_user.get("username")
            or self.current_user.get("UserLogin")
            or ""
        ).strip()
        self.security = str(self.current_user.get("usersecurity") or "").strip().casefold()
        self.user_unit = _unit_name(self.current_user.get("vahed"))
        self._columns: set[str] = set()
        self._rows_by_id: dict[str, dict] = {}
        self._search_after = None
        self._build_ui()
        self._load_unit_choices()
        self._load_topic_choices()
        self._set_new_request_number()
        self.refresh_list()

    def _build_ui(self) -> None:
        self.columnconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)

        form = ttk.LabelFrame(self, text=rtl_text("ثبت درخواست جدید"), padding=(14, 12))
        form.grid(row=0, column=0, sticky="ew", pady=(0, 12))
        form.columnconfigure(1, weight=1)
        form.columnconfigure(3, weight=1)

        self.number_var = tk.StringVar()
        self.date_var = tk.StringVar(value=jdatetime.date.today().strftime("%Y/%m/%d"))
        self.unit_var = tk.StringVar()
        self.topic_var = tk.StringVar()
        self.workplace_var = tk.StringVar()
        self.subplace_var = tk.StringVar()

        self._add_label(form, "شماره درخواست", 0, 0)
        self.number_entry = ttk.Entry(form, textvariable=self.number_var, justify="right", state="readonly")
        self.number_entry.grid(row=0, column=1, sticky="ew", padx=(8, 18), pady=6)

        self._add_label(form, "تاریخ درخواست (شمسی)", 0, 2)
        self.date_entry = ttk.Entry(form, textvariable=self.date_var, justify="right")
        self.date_entry.grid(row=0, column=3, sticky="ew", padx=8, pady=6)

        self._add_label(form, "واحد متقاضی", 1, 0)
        self.unit_combo = ttk.Combobox(form, textvariable=self.unit_var, justify="right", state="readonly")
        self.unit_combo.grid(row=1, column=1, sticky="ew", padx=(8, 18), pady=6)

        self._add_label(form, "موضوع درخواست", 1, 2)
        self.topic_combo = ttk.Combobox(form, textvariable=self.topic_var, justify="right", state="normal")
        self.topic_combo.grid(row=1, column=3, sticky="ew", padx=8, pady=6)

        self._add_label(form, "محل کار", 2, 0)
        self.workplace_entry = ttk.Entry(form, textvariable=self.workplace_var, justify="right")
        self.workplace_entry.grid(row=2, column=1, sticky="ew", padx=(8, 18), pady=6)

        self._add_label(form, "محل انجام کار / فرعی", 2, 2)
        self.subplace_entry = ttk.Entry(form, textvariable=self.subplace_var, justify="right")
        self.subplace_entry.grid(row=2, column=3, sticky="ew", padx=8, pady=6)

        self._add_label(form, "شرح درخواست", 3, 0)
        self.description = tk.Text(
            form, height=4, wrap="word", font=("Tahoma", 10),
            relief="solid", bd=1, padx=8, pady=7,
            background="#FFFFFF", foreground=COLORS["text"],
        )
        self.description.grid(row=3, column=1, columnspan=3, sticky="ew", padx=8, pady=6)
        self.description.tag_configure("rtl", justify="right")
        self.description.bind("<KeyRelease>", self._align_description)
        self.description.bind("<FocusIn>", self._align_description)

        actions = ttk.Frame(form, style="Surface.TFrame")
        actions.grid(row=4, column=0, columnspan=4, sticky="ew", pady=(8, 0))
        ttk.Button(actions, text=rtl_text("ثبت درخواست"), style="Primary.TButton", command=self.save_request).pack(side="right", padx=(6, 0))
        ttk.Button(actions, text=rtl_text("درخواست جدید / پاک کردن"), command=self.new_request).pack(side="right", padx=6)
        ttk.Button(actions, text=rtl_text("تازه‌سازی فهرست"), command=self.refresh_list).pack(side="left", padx=6)

        toolbar = ttk.Frame(self, style="Surface.TFrame")
        toolbar.grid(row=1, column=0, sticky="ew", pady=(0, 8))
        toolbar.columnconfigure(1, weight=1)
        ttk.Label(toolbar, text=rtl_text("جست‌وجو در درخواست‌ها:"), anchor="e").grid(row=0, column=2, sticky="e", padx=(8, 4))
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(toolbar, textvariable=self.search_var, justify="right")
        self.search_entry.grid(row=0, column=1, sticky="ew", padx=6)
        self.search_var.trace_add("write", self._schedule_search)
        ttk.Button(toolbar, text=rtl_text("پاک کردن جست‌وجو"), command=lambda: self.search_var.set("")).grid(row=0, column=0, padx=6)

        self.status_var = tk.StringVar(value="آماده")
        status = ttk.Label(self, textvariable=self.status_var, style="Muted.TLabel", anchor="e", justify="right")
        status.grid(row=2, column=0, sticky="ew", pady=(0, 6))

        table_frame = ttk.Frame(self, style="Surface.TFrame")
        table_frame.grid(row=3, column=0, sticky="nsew")
        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)

        self.tree = ttk.Treeview(
            table_frame,
            columns=("row", "number", "unit", "date", "topic", "workplace", "subplace", "requester", "description", "status", "follow_date", "follow_desc"),
            show="headings", selectmode="browse",
        )
        headings = {
            "row": "ردیف", "number": "شماره درخواست", "unit": "واحد",
            "date": "تاریخ درخواست", "topic": "موضوع", "workplace": "محل کار",
            "subplace": "محل کار فرعی", "requester": "درخواست‌کننده",
            "description": "شرح درخواست", "status": "وضعیت",
            "follow_date": "تاریخ پیگیری", "follow_desc": "شرح پیگیری",
        }
        widths = {
            "row": 55, "number": 105, "unit": 145, "date": 105, "topic": 120,
            "workplace": 130, "subplace": 130, "requester": 115,
            "description": 260, "status": 110, "follow_date": 105, "follow_desc": 220,
        }
        for col, title in headings.items():
            self.tree.heading(col, text=rtl_text(title), anchor="e")
            self.tree.column(col, width=widths[col], minwidth=65, anchor="e", stretch=True)
        self.tree.grid(row=0, column=0, sticky="nsew")
        yscroll = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        yscroll.grid(row=0, column=1, sticky="ns")
        xscroll = ttk.Scrollbar(table_frame, orient="horizontal", command=self.tree.xview)
        xscroll.grid(row=1, column=0, sticky="ew")
        self.tree.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
        self.tree.tag_configure("even", background="#FFFFFF")
        self.tree.tag_configure("odd", background="#F3F6FB")
        self.tree.bind("<<TreeviewSelect>>", self._show_selected_summary)

        self.selection_var = tk.StringVar(value="برای مشاهده خلاصه، یک درخواست را از جدول انتخاب کنید.")
        ttk.Label(self, textvariable=self.selection_var, anchor="e", justify="right", wraplength=1200).grid(row=4, column=0, sticky="ew", pady=(8, 0))

    @staticmethod
    def _add_label(parent, text, row, col) -> None:
        ttk.Label(parent, text=rtl_text(text), anchor="e", justify="right").grid(
            row=row, column=col, sticky="e", padx=6, pady=6
        )

    def _align_description(self, _event=None) -> None:
        self.description.tag_add("rtl", "1.0", "end")

    def _load_unit_choices(self) -> None:
        units = []
        conn = cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT DISTINCT [vahed] FROM [tblkar] "
                "WHERE [vahed] IS NOT NULL AND Trim([vahed]) <> '' ORDER BY [vahed]"
            )
            units = [_unit_name(row[0]) for row in cursor.fetchall() if row[0]]
        except Exception:
            units = []
        finally:
            self._close_db(cursor, conn)

        units = list(dict.fromkeys(units + list(UNIT_NAMES.values())))
        if self.security != "superadmin" and self.user_unit:
            units = [self.user_unit]
            self.unit_combo.configure(state="disabled")
        else:
            self.unit_combo.configure(state="readonly")
        self.unit_combo["values"] = units
        if self.user_unit and self.user_unit in units:
            self.unit_var.set(self.user_unit)
        elif units:
            self.unit_var.set(units[0])

    def _load_topic_choices(self) -> None:
        topics = []
        conn = cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT DISTINCT [mozooe] FROM [tblkar] "
                "WHERE [mozooe] IS NOT NULL AND Trim([mozooe]) <> '' ORDER BY [mozooe]"
            )
            topics = [str(row[0]).strip() for row in cursor.fetchall() if row[0] and str(row[0]).strip()]
        except Exception:
            topics = []
        finally:
            self._close_db(cursor, conn)
        if not topics:
            topics = ["برق", "مکانیک", "تأسیسات", "ساختمانی", "ابزار دقیق", "سایر"]
        self.topic_combo["values"] = list(dict.fromkeys(topics))

    @staticmethod
    def _close_db(cursor, conn) -> None:
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                pass
        if conn is not None:
            try:
                conn.close()
            except Exception:
                pass

    def _read_columns(self, cursor) -> set[str]:
        try:
            return {
                str(getattr(col, "column_name", "")).casefold()
                for col in cursor.columns(table="tblkar")
                if getattr(col, "column_name", None)
            }
        except Exception:
            return set()

    def _set_new_request_number(self) -> None:
        conn = cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT MAX([wonumber]) FROM [tblkar]")
            row = cursor.fetchone()
            next_number = int(row[0]) + 1 if row and row[0] is not None else 1
            self.number_var.set(str(next_number))
            self.status_var.set("شماره درخواست جدید آماده است.")
        except Exception as exc:
            self.number_var.set("پس از اتصال به شبکه")
            self.status_var.set("دیتابیس در دسترس نیست؛ پس از اتصال به شبکه، شماره درخواست دریافت می‌شود.")
        finally:
            self._close_db(cursor, conn)

    def new_request(self) -> None:
        self.date_var.set(jdatetime.date.today().strftime("%Y/%m/%d"))
        self.topic_var.set("")
        self.workplace_var.set("")
        self.subplace_var.set("")
        self.description.delete("1.0", "end")
        if self.security != "superadmin" and self.user_unit:
            self.unit_var.set(self.user_unit)
        self._set_new_request_number()
        self.selection_var.set("فرم برای ثبت درخواست جدید آماده است.")

    def _validate_form(self):
        number = self.number_var.get().strip()
        date_text = _normalize_digits(self.date_var.get()).strip()
        date_digits = "".join(ch for ch in date_text if ch.isdigit())
        unit = self.unit_var.get().strip()
        topic = self.topic_var.get().strip()
        workplace = self.workplace_var.get().strip()
        subplace = self.subplace_var.get().strip()
        description = self.description.get("1.0", "end").strip()

        if not number or not number.isdigit():
            raise ValueError("شماره درخواست معتبر نیست. ابتدا فهرست را تازه‌سازی کنید.")
        if len(date_digits) != 8:
            raise ValueError("تاریخ درخواست را به شکل 1405/07/18 وارد کنید.")
        try:
            jdatetime.date(int(date_digits[:4]), int(date_digits[4:6]), int(date_digits[6:8]))
        except ValueError:
            raise ValueError("تاریخ شمسی واردشده معتبر نیست.")
        if not unit:
            raise ValueError("واحد متقاضی را انتخاب کنید.")
        if not topic:
            raise ValueError("موضوع درخواست را وارد یا انتخاب کنید.")
        if not workplace:
            raise ValueError("محل کار را وارد کنید.")
        if not description:
            raise ValueError("شرح درخواست را وارد کنید.")
        if self.security != "superadmin" and unit != self.user_unit:
            raise PermissionError("شما فقط مجاز به ثبت درخواست برای واحد خود هستید.")

        return {
            "wonumber": number,
            "vahed": unit,
            "tarikhdarkhast": int(date_digits),
            "mozooe": topic,
            "mahalkarf": workplace,
            "mahalkara": subplace,
            "sharh": description,
            "darkhastkonande": self.username,
        }

    def save_request(self) -> None:
        try:
            values = self._validate_form()
        except (ValueError, PermissionError) as exc:
            messagebox.showwarning("بررسی اطلاعات درخواست", str(exc), parent=self.winfo_toplevel())
            return

        conn = cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            self._columns = self._read_columns(cursor)

            # ستون‌های پایه همان ستون‌های استفاده‌شده در نسخه قبلی هستند.
            insert_values = dict(values)
            optional_values = {
                "vaziyat": "ثبت نشده",
                "payan": False,
                "tarikh": None,
                "tarikhpey": None,
                "editor": self.username,
                "sharhepey": "",
            }
            for name, value in optional_values.items():
                if not self._columns or name.casefold() in self._columns:
                    # اگر هر دو نام قدیمی و جدید تاریخ پیگیری وجود داشته باشند،
                    # فقط ستون tarikh را برای جلوگیری از دوگانگی مقداردهی می‌کنیم.
                    if name == "tarikhpey" and "tarikh" in self._columns:
                        continue
                    if name == "tarikh" and "tarikhpey" in self._columns:
                        continue
                    insert_values[name] = value

            names = list(insert_values)
            sql_columns = ", ".join(f"[{name}]" for name in names)
            placeholders = ", ".join("?" for _ in names)
            cursor.execute(
                f"INSERT INTO [tblkar] ({sql_columns}) VALUES ({placeholders})",
                tuple(insert_values[name] for name in names),
            )
            conn.commit()
            self.status_var.set(f"درخواست شماره {values['wonumber']} با موفقیت ثبت شد.")
            messagebox.showinfo("ثبت درخواست", "درخواست با موفقیت ثبت شد.", parent=self.winfo_toplevel())
            self._load_topic_choices()
            self.refresh_list()
            self.new_request()
        except Exception as exc:
            if conn is not None:
                try:
                    conn.rollback()
                except Exception:
                    pass
            messagebox.showerror("خطا در ثبت درخواست", f"ثبت درخواست انجام نشد:\n{exc}", parent=self.winfo_toplevel())
            self.status_var.set("ثبت درخواست ناموفق بود.")
        finally:
            self._close_db(cursor, conn)

    def _schedule_search(self, *_args) -> None:
        if self._search_after is not None:
            try:
                self.after_cancel(self._search_after)
            except Exception:
                pass
        self._search_after = self.after(350, self.refresh_list)

    def refresh_list(self) -> None:
        if not self.winfo_exists():
            return
        if self._search_after is not None:
            try:
                self.after_cancel(self._search_after)
            except Exception:
                pass
            self._search_after = None

        for item in self.tree.get_children():
            self.tree.delete(item)
        self._rows_by_id.clear()

        conn = cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            self._columns = self._read_columns(cursor)
            optional = {
                "vaziyat": "'ثبت نشده' AS [vaziyat]",
                "tarikh": "NULL AS [tarikh]",
                "tarikhpey": "NULL AS [tarikhpey]",
                "sharhepey": "'' AS [sharhepey]",
            }
            selected_names = list(CORE_COLUMNS)
            select_expressions = [f"[{name}]" for name in CORE_COLUMNS]
            for name in ("vaziyat", "tarikh", "tarikhpey", "sharhepey"):
                if self._columns and name in self._columns:
                    if name == "tarikhpey" and "tarikh" in self._columns:
                        continue
                    if name == "tarikh" and "tarikhpey" in self._columns:
                        continue
                    selected_names.append(name)
                    select_expressions.append(f"[{name}]")
                elif self._columns:
                    selected_names.append(name)
                    select_expressions.append(optional[name])

            sql = "SELECT " + ", ".join(select_expressions) + " FROM [tblkar]"
            conditions = []
            params = []

            if self.security == "admin":
                if self.user_unit:
                    conditions.append("[vahed] = ?")
                    params.append(self.user_unit)
                else:
                    conditions.append("1 = 0")
            elif self.security != "superadmin":
                conditions.append("[darkhastkonande] = ?")
                params.append(self.username)

            search = self.search_var.get().strip()
            if search:
                like_fields = ["[vahed]", "[mozooe]", "[mahalkarf]", "[mahalkara]", "[sharh]", "[darkhastkonande]"]
                conditions.append("(" + " OR ".join(f"{field} LIKE ?" for field in like_fields) + " OR CStr([wonumber]) LIKE ?)")
                params.extend([f"%{search}%"] * (len(like_fields) + 1))

            if conditions:
                sql += " WHERE " + " AND ".join(conditions)
            order_col = "[id]" if not self._columns or "id" in self._columns else "[wonumber]"
            sql += f" ORDER BY {order_col} DESC"
            cursor.execute(sql, tuple(params))
            rows = cursor.fetchall()

            for index, row in enumerate(rows, start=1):
                data = dict(zip(selected_names, row))
                follow_date = data.get("tarikh") or data.get("tarikhpey") or ""
                values = [
                    index, data.get("wonumber", ""), data.get("vahed", ""),
                    _display_date(data.get("tarikhdarkhast")), data.get("mozooe", ""),
                    data.get("mahalkarf", ""), data.get("mahalkara", ""),
                    data.get("darkhastkonande", ""), data.get("sharh", ""),
                    data.get("vaziyat", "ثبت نشده") or "ثبت نشده",
                    _display_date(follow_date), data.get("sharhepey", ""),
                ]
                iid = str(index)
                self._rows_by_id[iid] = data
                shown = tuple(rtl_text(value) for value in values)
                self.tree.insert("", "end", iid=iid, values=shown, tags=("even" if index % 2 == 0 else "odd",))

            self.status_var.set(f"تعداد درخواست‌های قابل مشاهده: {len(rows)}")
        except Exception as exc:
            self.status_var.set("دریافت فهرست ناموفق بود؛ اتصال دیتابیس و ساختار tblkar را بررسی کنید.")
            # در حالت قطع شبکه پیام دائمی و مزاحم نمایش نمی‌دهیم؛ خطا در نوار وضعیت دیده می‌شود.
            self._last_load_error = str(exc)

    def _show_selected_summary(self, _event=None) -> None:
        selection = self.tree.selection()
        if not selection:
            return
        row = self._rows_by_id.get(selection[0], {})
        number = row.get("wonumber", "")
        topic = row.get("mozooe", "")
        requester = row.get("darkhastkonande", "")
        status = row.get("vaziyat", "ثبت نشده") or "ثبت نشده"
        self.selection_var.set(
            rtl_text(f"درخواست {number} | موضوع: {topic} | درخواست‌کننده: {requester} | وضعیت: {status}")
        )
