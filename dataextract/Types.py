# -----------------------------------------------------------------------
# Copyright (c) 2012 Tableau Software, Incorporated
#                    and its licensors. All rights reserved.
# Protected by U.S. Patent 7,089,266; Patents Pending.
#
# Portions of the code
# Copyright (c) 2002 The Board of Trustees of the Leland Stanford
#                    Junior University. All rights reserved.
# -----------------------------------------------------------------------
# Types.py
# -----------------------------------------------------------------------
# WARNING: Computer generated file.  Do not hand modify.
from ctypes import c_int
from . import Libs

libs = Libs.LoadLibs()
tablib = libs.load_lib

class Type(object):
    INTEGER               = c_int.in_dll(tablib, "TAB_TYPE_Integer").value                          # TDE_DT_SINT64
    DOUBLE                = c_int.in_dll(tablib, "TAB_TYPE_Double").value                           # TDE_DT_DOUBLE
    BOOLEAN               = c_int.in_dll(tablib, "TAB_TYPE_Boolean").value                          # TDE_DT_BOOL
    DATE                  = c_int.in_dll(tablib, "TAB_TYPE_Date").value                             # TDE_DT_DATE
    DATETIME              = c_int.in_dll(tablib, "TAB_TYPE_DateTime").value                         # TDE_DT_DATETIME
    DURATION              = c_int.in_dll(tablib, "TAB_TYPE_Duration").value                         # TDE_DT_DURATION
    CHAR_STRING           = c_int.in_dll(tablib, "TAB_TYPE_CharString").value                       # TDE_DT_STR
    UNICODE_STRING        = c_int.in_dll(tablib, "TAB_TYPE_UnicodeString").value                    # TDE_DT_WSTR

class Result(object):
    SUCCESS               = c_int.in_dll(tablib, "TAB_RESULT_Success").value                        # Successful function call
    OUT_OF_MEMORY         = c_int.in_dll(tablib, "TAB_RESULT_OutOfMemory").value                    # 
    PERMISSION_DENIED     = c_int.in_dll(tablib, "TAB_RESULT_PermissionDenied").value               # 
    INVALID_FILE          = c_int.in_dll(tablib, "TAB_RESULT_InvalidFile").value                    # 
    FILE_EXISTS           = c_int.in_dll(tablib, "TAB_RESULT_FileExists").value                     # 
    TOO_MANY_FILES        = c_int.in_dll(tablib, "TAB_RESULT_TooManyFiles").value                   # 
    FILE_NOT_FOUND        = c_int.in_dll(tablib, "TAB_RESULT_FileNotFound").value                   # 
    FISK_FULL             = c_int.in_dll(tablib, "TAB_RESULT_DiskFull").value                       # 
    DIRECTORY_NOT_EMPTY   = c_int.in_dll(tablib, "TAB_RESULT_DirectoryNotEmpty").value              # 
    NO_SUCH_DATABASE      = c_int.in_dll(tablib, "TAB_RESULT_NoSuchDatabase").value                 # Data Engine errors start at 200.
    QUERY_ERROR           = c_int.in_dll(tablib, "TAB_RESULT_QueryError").value                     # 
    NULL_ARGUMENT         = c_int.in_dll(tablib, "TAB_RESULT_NullArgument").value                   # 
    DATA_ENGINE_ERROR     = c_int.in_dll(tablib, "TAB_RESULT_DataEngineError").value                # 
    CANCELLED             = c_int.in_dll(tablib, "TAB_RESULT_Cancelled").value                      # 
    BAD_INDEX             = c_int.in_dll(tablib, "TAB_RESULT_BadIndex").value                       # 
    PROTOCOL_ERROR        = c_int.in_dll(tablib, "TAB_RESULT_ProtocolError").value                  # 
    NETWORK_ERROR         = c_int.in_dll(tablib, "TAB_RESULT_NetworkError").value                   # 
    INTERNAL_ERROR        = c_int.in_dll(tablib, "TAB_RESULT_InternalError").value                  # 300+: other error codes
    WRONG_TYPE            = c_int.in_dll(tablib, "TAB_RESULT_WrongType").value                      # 
    USAGE_ERROR           = c_int.in_dll(tablib, "TAB_RESULT_UsageError").value                     # 
    INVALID_ARGUMENT      = c_int.in_dll(tablib, "TAB_RESULT_InvalidArgument").value                # 
    BAD_HANDLE            = c_int.in_dll(tablib, "TAB_RESULT_BadHandle").value                      # 
    UNKNOWN_ERROR         = c_int.in_dll(tablib, "TAB_RESULT_UnknownError").value                   # 

class Collation(object):
    BINARY                = c_int.in_dll(tablib, "TAB_COLLATION_Binary").value                      # Internal binary representation
    AR                    = c_int.in_dll(tablib, "TAB_COLLATION_ar").value                          # Arabic
    CS                    = c_int.in_dll(tablib, "TAB_COLLATION_cs").value                          # Czech
    CS_CI                 = c_int.in_dll(tablib, "TAB_COLLATION_cs_CI").value                       # Czech (Case Insensitive)
    CS_CI_AI              = c_int.in_dll(tablib, "TAB_COLLATION_cs_CI_AI").value                    # Czech (Case/Accent Insensitive
    DA                    = c_int.in_dll(tablib, "TAB_COLLATION_da").value                          # Danish
    DE                    = c_int.in_dll(tablib, "TAB_COLLATION_de").value                          # German
    EL                    = c_int.in_dll(tablib, "TAB_COLLATION_el").value                          # Greek
    EN_GB                 = c_int.in_dll(tablib, "TAB_COLLATION_en_GB").value                       # English (Great Britain)
    EN_US                 = c_int.in_dll(tablib, "TAB_COLLATION_en_US").value                       # English (US)
    EN_US_CI              = c_int.in_dll(tablib, "TAB_COLLATION_en_US_CI").value                    # English (US, Case Insensitive)
    ES                    = c_int.in_dll(tablib, "TAB_COLLATION_es").value                          # Spanish
    ES_CI_AI              = c_int.in_dll(tablib, "TAB_COLLATION_es_CI_AI").value                    # Spanish (Case/Accent Insensitive)
    ET                    = c_int.in_dll(tablib, "TAB_COLLATION_et").value                          # Estonian
    FI                    = c_int.in_dll(tablib, "TAB_COLLATION_fi").value                          # Finnish
    FR_CA                 = c_int.in_dll(tablib, "TAB_COLLATION_fr_CA").value                       # French (Canada)
    FR_FR                 = c_int.in_dll(tablib, "TAB_COLLATION_fr_FR").value                       # French (France)
    FR_FR_CI_AI           = c_int.in_dll(tablib, "TAB_COLLATION_fr_FR_CI_AI").value                 # French (France, Case/Accent Insensitive)
    HE                    = c_int.in_dll(tablib, "TAB_COLLATION_he").value                          # Hebrew
    HU                    = c_int.in_dll(tablib, "TAB_COLLATION_hu").value                          # Hungarian
    IS                    = c_int.in_dll(tablib, "TAB_COLLATION_is").value                          # Icelandic
    IT                    = c_int.in_dll(tablib, "TAB_COLLATION_it").value                          # Italian
    JA                    = c_int.in_dll(tablib, "TAB_COLLATION_ja").value                          # Japanese
    JA_JIS                = c_int.in_dll(tablib, "TAB_COLLATION_ja_JIS").value                      # Japanese (JIS)
    KO                    = c_int.in_dll(tablib, "TAB_COLLATION_ko").value                          # Korean
    LT                    = c_int.in_dll(tablib, "TAB_COLLATION_lt").value                          # Lithuanian
    LV                    = c_int.in_dll(tablib, "TAB_COLLATION_lv").value                          # Latvian
    NL_NL                 = c_int.in_dll(tablib, "TAB_COLLATION_nl_NL").value                       # Dutch (Netherlands)
    NN                    = c_int.in_dll(tablib, "TAB_COLLATION_nn").value                          # Norwegian
    PL                    = c_int.in_dll(tablib, "TAB_COLLATION_pl").value                          # Polish
    PT_BR                 = c_int.in_dll(tablib, "TAB_COLLATION_pt_BR").value                       # Portuguese (Brazil)
    PT_BR_CI_AI           = c_int.in_dll(tablib, "TAB_COLLATION_pt_BR_CI_AI").value                 # Portuguese (Brazil Case/Accent Insensitive)
    PT_PT                 = c_int.in_dll(tablib, "TAB_COLLATION_pt_PT").value                       # Portuguese (Portugal)
    ROOT                  = c_int.in_dll(tablib, "TAB_COLLATION_root").value                        # Root
    RU                    = c_int.in_dll(tablib, "TAB_COLLATION_ru").value                          # Russian
    SL                    = c_int.in_dll(tablib, "TAB_COLLATION_sl").value                          # Slovenian
    SV_FI                 = c_int.in_dll(tablib, "TAB_COLLATION_sv_FI").value                       # Swedish (Finland)
    SV_SE                 = c_int.in_dll(tablib, "TAB_COLLATION_sv_SE").value                       # Swedish (Sweden)
    TR                    = c_int.in_dll(tablib, "TAB_COLLATION_tr").value                          # Turkish
    UK                    = c_int.in_dll(tablib, "TAB_COLLATION_uk").value                          # Ukrainian
    VI                    = c_int.in_dll(tablib, "TAB_COLLATION_vi").value                          # Vietnamese
    ZH_HANS_CN            = c_int.in_dll(tablib, "TAB_COLLATION_zh_Hans_CN").value                  # Chinese (Simplified, China)
    ZH_HANT_TW            = c_int.in_dll(tablib, "TAB_COLLATION_zh_Hant_TW").value                  # Chinese (Traditional, Taiwan)
