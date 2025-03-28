# generated from instructions.py.mako
# do not edit manually!
from micropython import const
from typing import TYPE_CHECKING

from trezor.wire import DataError

from apps.common.readers import read_uint32_le, read_uint64_le

from ..format import (
    format_identity,
    format_int,
    format_lamports,
    format_pubkey,
    format_token_amount,
    format_unix_timestamp,
)
from ..types import AccountTemplate, PropertyTemplate, UIProperty
from .instruction import Instruction
from .parse import parse_byte, parse_memo, parse_pubkey, parse_string

if TYPE_CHECKING:
    from typing import Any, Type, TypeGuard

    from ..types import Account, InstructionData, InstructionId

_SYSTEM_PROGRAM_ID = "11111111111111111111111111111111"
_STAKE_PROGRAM_ID = "Stake11111111111111111111111111111111111111"
_COMPUTE_BUDGET_PROGRAM_ID = "ComputeBudget111111111111111111111111111111"
_TOKEN_PROGRAM_ID = "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
_TOKEN_2022_PROGRAM_ID = "TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb"
_ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID = "ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL"
_MEMO_PROGRAM_ID = "MemoSq4gqABAXKb96qnH8TysNcWxMyWCqXgDLGmfcHr"
_MEMO_LEGACY_PROGRAM_ID = "Memo1UhkJRfHyvLMcVucJwxXeuD728EqVDDwQDxFMNo"

_SYSTEM_PROGRAM_ID_INS_CREATE_ACCOUNT = const(0)
_SYSTEM_PROGRAM_ID_INS_ASSIGN = const(1)
_SYSTEM_PROGRAM_ID_INS_TRANSFER = const(2)
_SYSTEM_PROGRAM_ID_INS_CREATE_ACCOUNT_WITH_SEED = const(3)
_SYSTEM_PROGRAM_ID_INS_ADVANCE_NONCE_ACCOUNT = const(4)
_SYSTEM_PROGRAM_ID_INS_WITHDRAW_NONCE_ACCOUNT = const(5)
_SYSTEM_PROGRAM_ID_INS_INITIALIZE_NONCE_ACCOUNT = const(6)
_SYSTEM_PROGRAM_ID_INS_AUTHORIZE_NONCE_ACCOUNT = const(7)
_SYSTEM_PROGRAM_ID_INS_ALLOCATE = const(8)
_SYSTEM_PROGRAM_ID_INS_ALLOCATE_WITH_SEED = const(9)
_SYSTEM_PROGRAM_ID_INS_ASSIGN_WITH_SEED = const(10)
_SYSTEM_PROGRAM_ID_INS_TRANSFER_WITH_SEED = const(11)
_SYSTEM_PROGRAM_ID_INS_UPGRADE_NONCE_ACCOUNT = const(12)
_STAKE_PROGRAM_ID_INS_INITIALIZE = const(0)
_STAKE_PROGRAM_ID_INS_AUTHORIZE = const(1)
_STAKE_PROGRAM_ID_INS_DELEGATE_STAKE = const(2)
_STAKE_PROGRAM_ID_INS_SPLIT = const(3)
_STAKE_PROGRAM_ID_INS_WITHDRAW = const(4)
_STAKE_PROGRAM_ID_INS_DEACTIVATE = const(5)
_STAKE_PROGRAM_ID_INS_SET_LOCKUP = const(6)
_STAKE_PROGRAM_ID_INS_MERGE = const(7)
_STAKE_PROGRAM_ID_INS_AUTHORIZE_WITH_SEED = const(8)
_STAKE_PROGRAM_ID_INS_INITIALIZE_CHECKED = const(9)
_STAKE_PROGRAM_ID_INS_AUTHORIZE_CHECKED = const(10)
_STAKE_PROGRAM_ID_INS_AUTHORIZE_CHECKED_WITH_SEED = const(11)
_STAKE_PROGRAM_ID_INS_SET_LOCKUP_CHECKED = const(12)
_COMPUTE_BUDGET_PROGRAM_ID_INS_REQUEST_HEAP_FRAME = const(1)
_COMPUTE_BUDGET_PROGRAM_ID_INS_SET_COMPUTE_UNIT_LIMIT = const(2)
_COMPUTE_BUDGET_PROGRAM_ID_INS_SET_COMPUTE_UNIT_PRICE = const(3)
_TOKEN_PROGRAM_ID_INS_INITIALIZE_ACCOUNT = const(1)
_TOKEN_PROGRAM_ID_INS_INITIALIZE_MULTISIG = const(2)
_TOKEN_PROGRAM_ID_INS_TRANSFER = const(3)
_TOKEN_PROGRAM_ID_INS_APPROVE = const(4)
_TOKEN_PROGRAM_ID_INS_REVOKE = const(5)
_TOKEN_PROGRAM_ID_INS_SET_AUTHORITY = const(6)
_TOKEN_PROGRAM_ID_INS_MINT_TO = const(7)
_TOKEN_PROGRAM_ID_INS_BURN = const(8)
_TOKEN_PROGRAM_ID_INS_CLOSE_ACCOUNT = const(9)
_TOKEN_PROGRAM_ID_INS_FREEZE_ACCOUNT = const(10)
_TOKEN_PROGRAM_ID_INS_THAW_ACCOUNT = const(11)
_TOKEN_PROGRAM_ID_INS_TRANSFER_CHECKED = const(12)
_TOKEN_PROGRAM_ID_INS_APPROVE_CHECKED = const(13)
_TOKEN_PROGRAM_ID_INS_MINT_TO_CHECKED = const(14)
_TOKEN_PROGRAM_ID_INS_BURN_CHECKED = const(15)
_TOKEN_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_2 = const(16)
_TOKEN_PROGRAM_ID_INS_SYNC_NATIVE = const(17)
_TOKEN_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_3 = const(18)
_TOKEN_PROGRAM_ID_INS_INITIALIZE_IMMUTABLE_OWNER = const(22)
_TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_ACCOUNT = const(1)
_TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_MULTISIG = const(2)
_TOKEN_2022_PROGRAM_ID_INS_TRANSFER = const(3)
_TOKEN_2022_PROGRAM_ID_INS_APPROVE = const(4)
_TOKEN_2022_PROGRAM_ID_INS_REVOKE = const(5)
_TOKEN_2022_PROGRAM_ID_INS_SET_AUTHORITY = const(6)
_TOKEN_2022_PROGRAM_ID_INS_MINT_TO = const(7)
_TOKEN_2022_PROGRAM_ID_INS_BURN = const(8)
_TOKEN_2022_PROGRAM_ID_INS_CLOSE_ACCOUNT = const(9)
_TOKEN_2022_PROGRAM_ID_INS_FREEZE_ACCOUNT = const(10)
_TOKEN_2022_PROGRAM_ID_INS_THAW_ACCOUNT = const(11)
_TOKEN_2022_PROGRAM_ID_INS_TRANSFER_CHECKED = const(12)
_TOKEN_2022_PROGRAM_ID_INS_APPROVE_CHECKED = const(13)
_TOKEN_2022_PROGRAM_ID_INS_MINT_TO_CHECKED = const(14)
_TOKEN_2022_PROGRAM_ID_INS_BURN_CHECKED = const(15)
_TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_2 = const(16)
_TOKEN_2022_PROGRAM_ID_INS_SYNC_NATIVE = const(17)
_TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_3 = const(18)
_TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_IMMUTABLE_OWNER = const(22)
_ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID_INS_CREATE = None
_ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID_INS_CREATE_IDEMPOTENT = const(1)
_ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID_INS_RECOVER_NESTED = const(2)
_MEMO_PROGRAM_ID_INS_MEMO = None
_MEMO_LEGACY_PROGRAM_ID_INS_MEMO = None

COMPUTE_BUDGET_PROGRAM_ID = _COMPUTE_BUDGET_PROGRAM_ID
COMPUTE_BUDGET_PROGRAM_ID_INS_SET_COMPUTE_UNIT_LIMIT = (
    _COMPUTE_BUDGET_PROGRAM_ID_INS_SET_COMPUTE_UNIT_LIMIT
)
COMPUTE_BUDGET_PROGRAM_ID_INS_SET_COMPUTE_UNIT_PRICE = (
    _COMPUTE_BUDGET_PROGRAM_ID_INS_SET_COMPUTE_UNIT_PRICE
)


def __getattr__(name: str) -> Type[Instruction]:
    def get_id(name: str) -> tuple[str, InstructionId]:
        if name == "SystemProgramCreateAccountInstruction":
            return (_SYSTEM_PROGRAM_ID, _SYSTEM_PROGRAM_ID_INS_CREATE_ACCOUNT)
        if name == "SystemProgramAssignInstruction":
            return (_SYSTEM_PROGRAM_ID, _SYSTEM_PROGRAM_ID_INS_ASSIGN)
        if name == "SystemProgramTransferInstruction":
            return (_SYSTEM_PROGRAM_ID, _SYSTEM_PROGRAM_ID_INS_TRANSFER)
        if name == "SystemProgramCreateAccountWithSeedInstruction":
            return (_SYSTEM_PROGRAM_ID, _SYSTEM_PROGRAM_ID_INS_CREATE_ACCOUNT_WITH_SEED)
        if name == "SystemProgramAdvanceNonceAccountInstruction":
            return (_SYSTEM_PROGRAM_ID, _SYSTEM_PROGRAM_ID_INS_ADVANCE_NONCE_ACCOUNT)
        if name == "SystemProgramWithdrawNonceAccountInstruction":
            return (_SYSTEM_PROGRAM_ID, _SYSTEM_PROGRAM_ID_INS_WITHDRAW_NONCE_ACCOUNT)
        if name == "SystemProgramInitializeNonceAccountInstruction":
            return (_SYSTEM_PROGRAM_ID, _SYSTEM_PROGRAM_ID_INS_INITIALIZE_NONCE_ACCOUNT)
        if name == "SystemProgramAuthorizeNonceAccountInstruction":
            return (_SYSTEM_PROGRAM_ID, _SYSTEM_PROGRAM_ID_INS_AUTHORIZE_NONCE_ACCOUNT)
        if name == "SystemProgramAllocateInstruction":
            return (_SYSTEM_PROGRAM_ID, _SYSTEM_PROGRAM_ID_INS_ALLOCATE)
        if name == "SystemProgramAllocateWithSeedInstruction":
            return (_SYSTEM_PROGRAM_ID, _SYSTEM_PROGRAM_ID_INS_ALLOCATE_WITH_SEED)
        if name == "SystemProgramAssignWithSeedInstruction":
            return (_SYSTEM_PROGRAM_ID, _SYSTEM_PROGRAM_ID_INS_ASSIGN_WITH_SEED)
        if name == "SystemProgramTransferWithSeedInstruction":
            return (_SYSTEM_PROGRAM_ID, _SYSTEM_PROGRAM_ID_INS_TRANSFER_WITH_SEED)
        if name == "SystemProgramUpgradeNonceAccountInstruction":
            return (_SYSTEM_PROGRAM_ID, _SYSTEM_PROGRAM_ID_INS_UPGRADE_NONCE_ACCOUNT)
        if name == "StakeProgramInitializeInstruction":
            return (_STAKE_PROGRAM_ID, _STAKE_PROGRAM_ID_INS_INITIALIZE)
        if name == "StakeProgramAuthorizeInstruction":
            return (_STAKE_PROGRAM_ID, _STAKE_PROGRAM_ID_INS_AUTHORIZE)
        if name == "StakeProgramDelegateStakeInstruction":
            return (_STAKE_PROGRAM_ID, _STAKE_PROGRAM_ID_INS_DELEGATE_STAKE)
        if name == "StakeProgramSplitInstruction":
            return (_STAKE_PROGRAM_ID, _STAKE_PROGRAM_ID_INS_SPLIT)
        if name == "StakeProgramWithdrawInstruction":
            return (_STAKE_PROGRAM_ID, _STAKE_PROGRAM_ID_INS_WITHDRAW)
        if name == "StakeProgramDeactivateInstruction":
            return (_STAKE_PROGRAM_ID, _STAKE_PROGRAM_ID_INS_DEACTIVATE)
        if name == "StakeProgramSetLockupInstruction":
            return (_STAKE_PROGRAM_ID, _STAKE_PROGRAM_ID_INS_SET_LOCKUP)
        if name == "StakeProgramMergeInstruction":
            return (_STAKE_PROGRAM_ID, _STAKE_PROGRAM_ID_INS_MERGE)
        if name == "StakeProgramAuthorizeWithSeedInstruction":
            return (_STAKE_PROGRAM_ID, _STAKE_PROGRAM_ID_INS_AUTHORIZE_WITH_SEED)
        if name == "StakeProgramInitializeCheckedInstruction":
            return (_STAKE_PROGRAM_ID, _STAKE_PROGRAM_ID_INS_INITIALIZE_CHECKED)
        if name == "StakeProgramAuthorizeCheckedInstruction":
            return (_STAKE_PROGRAM_ID, _STAKE_PROGRAM_ID_INS_AUTHORIZE_CHECKED)
        if name == "StakeProgramAuthorizeCheckedWithSeedInstruction":
            return (
                _STAKE_PROGRAM_ID,
                _STAKE_PROGRAM_ID_INS_AUTHORIZE_CHECKED_WITH_SEED,
            )
        if name == "StakeProgramSetLockupCheckedInstruction":
            return (_STAKE_PROGRAM_ID, _STAKE_PROGRAM_ID_INS_SET_LOCKUP_CHECKED)
        if name == "ComputeBudgetProgramRequestHeapFrameInstruction":
            return (
                _COMPUTE_BUDGET_PROGRAM_ID,
                _COMPUTE_BUDGET_PROGRAM_ID_INS_REQUEST_HEAP_FRAME,
            )
        if name == "ComputeBudgetProgramSetComputeUnitLimitInstruction":
            return (
                _COMPUTE_BUDGET_PROGRAM_ID,
                _COMPUTE_BUDGET_PROGRAM_ID_INS_SET_COMPUTE_UNIT_LIMIT,
            )
        if name == "ComputeBudgetProgramSetComputeUnitPriceInstruction":
            return (
                _COMPUTE_BUDGET_PROGRAM_ID,
                _COMPUTE_BUDGET_PROGRAM_ID_INS_SET_COMPUTE_UNIT_PRICE,
            )
        if name == "TokenProgramInitializeAccountInstruction":
            return (_TOKEN_PROGRAM_ID, _TOKEN_PROGRAM_ID_INS_INITIALIZE_ACCOUNT)
        if name == "TokenProgramInitializeMultisigInstruction":
            return (_TOKEN_PROGRAM_ID, _TOKEN_PROGRAM_ID_INS_INITIALIZE_MULTISIG)
        if name == "TokenProgramTransferInstruction":
            return (_TOKEN_PROGRAM_ID, _TOKEN_PROGRAM_ID_INS_TRANSFER)
        if name == "TokenProgramApproveInstruction":
            return (_TOKEN_PROGRAM_ID, _TOKEN_PROGRAM_ID_INS_APPROVE)
        if name == "TokenProgramRevokeInstruction":
            return (_TOKEN_PROGRAM_ID, _TOKEN_PROGRAM_ID_INS_REVOKE)
        if name == "TokenProgramSetAuthorityInstruction":
            return (_TOKEN_PROGRAM_ID, _TOKEN_PROGRAM_ID_INS_SET_AUTHORITY)
        if name == "TokenProgramMintToInstruction":
            return (_TOKEN_PROGRAM_ID, _TOKEN_PROGRAM_ID_INS_MINT_TO)
        if name == "TokenProgramBurnInstruction":
            return (_TOKEN_PROGRAM_ID, _TOKEN_PROGRAM_ID_INS_BURN)
        if name == "TokenProgramCloseAccountInstruction":
            return (_TOKEN_PROGRAM_ID, _TOKEN_PROGRAM_ID_INS_CLOSE_ACCOUNT)
        if name == "TokenProgramFreezeAccountInstruction":
            return (_TOKEN_PROGRAM_ID, _TOKEN_PROGRAM_ID_INS_FREEZE_ACCOUNT)
        if name == "TokenProgramThawAccountInstruction":
            return (_TOKEN_PROGRAM_ID, _TOKEN_PROGRAM_ID_INS_THAW_ACCOUNT)
        if name == "TokenProgramTransferCheckedInstruction":
            return (_TOKEN_PROGRAM_ID, _TOKEN_PROGRAM_ID_INS_TRANSFER_CHECKED)
        if name == "TokenProgramApproveCheckedInstruction":
            return (_TOKEN_PROGRAM_ID, _TOKEN_PROGRAM_ID_INS_APPROVE_CHECKED)
        if name == "TokenProgramMinttoCheckedInstruction":
            return (_TOKEN_PROGRAM_ID, _TOKEN_PROGRAM_ID_INS_MINT_TO_CHECKED)
        if name == "TokenProgramBurnCheckedInstruction":
            return (_TOKEN_PROGRAM_ID, _TOKEN_PROGRAM_ID_INS_BURN_CHECKED)
        if name == "TokenProgramInitializeAccount2Instruction":
            return (_TOKEN_PROGRAM_ID, _TOKEN_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_2)
        if name == "TokenProgramSyncNativeInstruction":
            return (_TOKEN_PROGRAM_ID, _TOKEN_PROGRAM_ID_INS_SYNC_NATIVE)
        if name == "TokenProgramInitializeAccount3Instruction":
            return (_TOKEN_PROGRAM_ID, _TOKEN_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_3)
        if name == "TokenProgramInitializeImmutableOwnerInstruction":
            return (_TOKEN_PROGRAM_ID, _TOKEN_PROGRAM_ID_INS_INITIALIZE_IMMUTABLE_OWNER)
        if name == "Token2022ProgramInitializeAccountInstruction":
            return (
                _TOKEN_2022_PROGRAM_ID,
                _TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_ACCOUNT,
            )
        if name == "Token2022ProgramInitializeMultisigInstruction":
            return (
                _TOKEN_2022_PROGRAM_ID,
                _TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_MULTISIG,
            )
        if name == "Token2022ProgramTransferInstruction":
            return (_TOKEN_2022_PROGRAM_ID, _TOKEN_2022_PROGRAM_ID_INS_TRANSFER)
        if name == "Token2022ProgramApproveInstruction":
            return (_TOKEN_2022_PROGRAM_ID, _TOKEN_2022_PROGRAM_ID_INS_APPROVE)
        if name == "Token2022ProgramRevokeInstruction":
            return (_TOKEN_2022_PROGRAM_ID, _TOKEN_2022_PROGRAM_ID_INS_REVOKE)
        if name == "Token2022ProgramSetAuthorityInstruction":
            return (_TOKEN_2022_PROGRAM_ID, _TOKEN_2022_PROGRAM_ID_INS_SET_AUTHORITY)
        if name == "Token2022ProgramMinttoInstruction":
            return (_TOKEN_2022_PROGRAM_ID, _TOKEN_2022_PROGRAM_ID_INS_MINT_TO)
        if name == "Token2022ProgramBurnInstruction":
            return (_TOKEN_2022_PROGRAM_ID, _TOKEN_2022_PROGRAM_ID_INS_BURN)
        if name == "Token2022ProgramCloseAccountInstruction":
            return (_TOKEN_2022_PROGRAM_ID, _TOKEN_2022_PROGRAM_ID_INS_CLOSE_ACCOUNT)
        if name == "Token2022ProgramFreezeAccountInstruction":
            return (_TOKEN_2022_PROGRAM_ID, _TOKEN_2022_PROGRAM_ID_INS_FREEZE_ACCOUNT)
        if name == "Token2022ProgramThawAccountInstruction":
            return (_TOKEN_2022_PROGRAM_ID, _TOKEN_2022_PROGRAM_ID_INS_THAW_ACCOUNT)
        if name == "Token2022ProgramTransferCheckedInstruction":
            return (_TOKEN_2022_PROGRAM_ID, _TOKEN_2022_PROGRAM_ID_INS_TRANSFER_CHECKED)
        if name == "Token2022ProgramApproveCheckedInstruction":
            return (_TOKEN_2022_PROGRAM_ID, _TOKEN_2022_PROGRAM_ID_INS_APPROVE_CHECKED)
        if name == "Token2022ProgramMinttoCheckedInstruction":
            return (_TOKEN_2022_PROGRAM_ID, _TOKEN_2022_PROGRAM_ID_INS_MINT_TO_CHECKED)
        if name == "Token2022ProgramBurnCheckedInstruction":
            return (_TOKEN_2022_PROGRAM_ID, _TOKEN_2022_PROGRAM_ID_INS_BURN_CHECKED)
        if name == "Token2022ProgramInitializeAccount2Instruction":
            return (
                _TOKEN_2022_PROGRAM_ID,
                _TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_2,
            )
        if name == "Token2022ProgramSyncNativeInstruction":
            return (_TOKEN_2022_PROGRAM_ID, _TOKEN_2022_PROGRAM_ID_INS_SYNC_NATIVE)
        if name == "Token2022ProgramInitializeAccount3Instruction":
            return (
                _TOKEN_2022_PROGRAM_ID,
                _TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_3,
            )
        if name == "Token2022ProgramInitializeImmutableOwnerInstruction":
            return (
                _TOKEN_2022_PROGRAM_ID,
                _TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_IMMUTABLE_OWNER,
            )
        if name == "AssociatedTokenAccountProgramCreateInstruction":
            return (
                _ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID,
                _ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID_INS_CREATE,
            )
        if name == "AssociatedTokenAccountProgramCreateIdempotentInstruction":
            return (
                _ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID,
                _ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID_INS_CREATE_IDEMPOTENT,
            )
        if name == "AssociatedTokenAccountProgramRecoverNestedInstruction":
            return (
                _ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID,
                _ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID_INS_RECOVER_NESTED,
            )
        if name == "MemoProgramMemoInstruction":
            return (_MEMO_PROGRAM_ID, _MEMO_PROGRAM_ID_INS_MEMO)
        if name == "MemoLegacyProgramMemoInstruction":
            return (_MEMO_LEGACY_PROGRAM_ID, _MEMO_LEGACY_PROGRAM_ID_INS_MEMO)
        raise AttributeError  # Unknown instruction

    id = get_id(name)

    class FakeClass(Instruction):
        @classmethod
        def is_type_of(cls, ins: Any) -> TypeGuard[Instruction]:
            return ins.program_id == id[0] and ins.instruction_id == id[1]

    return FakeClass


if TYPE_CHECKING:

    class SystemProgramCreateAccountInstruction(Instruction):
        lamports: int
        space: int
        owner: Account

        funding_account: Account
        new_account: Account

    class SystemProgramAssignInstruction(Instruction):
        owner: Account

        assigned_account: Account

    class SystemProgramTransferInstruction(Instruction):
        lamports: int

        funding_account: Account
        recipient_account: Account

    class SystemProgramCreateAccountWithSeedInstruction(Instruction):
        base: int
        seed: str
        lamports: int
        space: int
        owner: int

        funding_account: Account
        created_account: Account
        base_account: Account | None

    class SystemProgramAdvanceNonceAccountInstruction(Instruction):

        nonce_account: Account
        recent_blockhashes_sysvar: Account
        nonce_authority: Account

    class SystemProgramWithdrawNonceAccountInstruction(Instruction):
        lamports: int

        nonce_account: Account
        recipient_account: Account
        recent_blockhashes_sysvar: Account
        rent_sysvar: Account
        nonce_authority: Account

    class SystemProgramInitializeNonceAccountInstruction(Instruction):
        nonce_authority: Account

        nonce_account: Account
        recent_blockhashes_sysvar: Account
        rent_sysvar: Account

    class SystemProgramAuthorizeNonceAccountInstruction(Instruction):
        nonce_authority: Account

        nonce_account: Account
        nonce_authority: Account

    class SystemProgramAllocateInstruction(Instruction):
        space: int

        new_account: Account

    class SystemProgramAllocateWithSeedInstruction(Instruction):
        base: int
        seed: str
        space: int
        owner: int

        allocated_account: Account
        base_account: Account

    class SystemProgramAssignWithSeedInstruction(Instruction):
        base: int
        seed: str
        owner: int

        assigned_account: Account
        base_account: Account

    class SystemProgramTransferWithSeedInstruction(Instruction):
        lamports: int
        from_seed: str
        from_owner: int

        funding_account: Account
        base_account: Account
        recipient_account: Account

    class SystemProgramUpgradeNonceAccountInstruction(Instruction):

        nonce_account: Account

    class StakeProgramInitializeInstruction(Instruction):
        staker: Account
        withdrawer: Account
        unix_timestamp: int
        epoch: int
        custodian: Account

        uninitialized_stake_account: Account
        rent_sysvar: Account

    class StakeProgramAuthorizeInstruction(Instruction):
        pubkey: int
        stake_authorize: int

        stake_account: Account
        clock_sysvar: Account
        stake_or_withdraw_authority: Account
        lockup_authority: Account | None

    class StakeProgramDelegateStakeInstruction(Instruction):

        initialized_stake_account: Account
        vote_account: Account
        clock_sysvar: Account
        stake_history_sysvar: Account
        config_account: Account
        stake_authority: Account

    class StakeProgramSplitInstruction(Instruction):
        lamports: int

        stake_account: Account
        uninitialized_stake_account: Account
        stake_authority: Account

    class StakeProgramWithdrawInstruction(Instruction):
        lamports: int

        stake_account: Account
        recipient_account: Account
        clock_sysvar: Account
        stake_history_sysvar: Account
        withdrawal_authority: Account
        lockup_authority: Account | None

    class StakeProgramDeactivateInstruction(Instruction):

        delegated_stake_account: Account
        clock_sysvar: Account
        stake_authority: Account

    class StakeProgramSetLockupInstruction(Instruction):
        unix_timestamp: int
        epoch: int
        custodian: int

        initialized_stake_account: Account
        lockup_or_withdraw_authority: Account

    class StakeProgramMergeInstruction(Instruction):

        destination_stake_account: Account
        source_stake_account: Account
        clock_sysvar: Account
        stake_history_sysvar: Account
        stake_authority: Account

    class StakeProgramAuthorizeWithSeedInstruction(Instruction):
        new_authorized_pubkey: int
        stake_authorize: int
        authority_seed: str
        authority_owner: int

        stake_account: Account
        stake_or_withdraw_authority: Account
        clock_sysvar: Account
        lockup_authority: Account | None

    class StakeProgramInitializeCheckedInstruction(Instruction):

        uninitialized_stake_account: Account
        rent_sysvar: Account
        stake_authority: Account
        withdrawal_authority: Account

    class StakeProgramAuthorizeCheckedInstruction(Instruction):
        stake_authorize: int

        stake_account: Account
        clock_sysvar: Account
        stake_or_withdraw_authority: Account
        new_stake_or_withdraw_authority: Account
        lockup_authority: Account | None

    class StakeProgramAuthorizeCheckedWithSeedInstruction(Instruction):
        stake_authorize: int
        authority_seed: str
        authority_owner: int

        stake_account: Account
        stake_or_withdraw_authority: Account
        clock_sysvar: Account
        new_stake_or_withdraw_authority: Account
        lockup_authority: Account | None

    class StakeProgramSetLockupCheckedInstruction(Instruction):
        unix_timestamp: int
        epoch: int

        stake_account: Account
        lockup_or_withdraw_authority: Account
        new_lockup_authority: Account | None

    class ComputeBudgetProgramRequestHeapFrameInstruction(Instruction):
        bytes: int

    class ComputeBudgetProgramSetComputeUnitLimitInstruction(Instruction):
        units: int

    class ComputeBudgetProgramSetComputeUnitPriceInstruction(Instruction):
        lamports: int

    class TokenProgramInitializeAccountInstruction(Instruction):

        account_to_initialize: Account
        mint_account: Account
        owner: Account
        rent_sysvar: Account

    class TokenProgramInitializeMultisigInstruction(Instruction):
        number_of_signers: int

        multisig_account: Account
        rent_sysvar: Account
        signer_accounts: Account

    class TokenProgramTransferInstruction(Instruction):
        amount: int

        source_account: Account
        destination_account: Account
        owner: Account

    class TokenProgramApproveInstruction(Instruction):
        amount: int

        source_account: Account
        delegate_account: Account
        owner: Account

    class TokenProgramRevokeInstruction(Instruction):

        source_account: Account
        owner: Account

    class TokenProgramSetAuthorityInstruction(Instruction):
        authority_type: int
        new_authority: Account

        mint_account: Account
        current_authority: Account

    class TokenProgramMintToInstruction(Instruction):
        amount: int

        mint: Account
        account_to_mint: Account
        minting_authority: Account

    class TokenProgramBurnInstruction(Instruction):
        amount: int

        account_to_burn_from: Account
        token_mint: Account
        owner: Account

    class TokenProgramCloseAccountInstruction(Instruction):

        account_to_close: Account
        destination_account: Account
        owner: Account

    class TokenProgramFreezeAccountInstruction(Instruction):

        account_to_freeze: Account
        token_mint: Account
        freeze_authority: Account

    class TokenProgramThawAccountInstruction(Instruction):

        account_to_freeze: Account
        token_mint: Account
        freeze_authority: Account

    class TokenProgramTransferCheckedInstruction(Instruction):
        amount: int
        decimals: int

        source_account: Account
        token_mint: Account
        destination_account: Account
        owner: Account

    class TokenProgramApproveCheckedInstruction(Instruction):
        amount: int
        decimals: int

        source_account: Account
        token_mint: Account
        delegate: Account
        owner: Account

    class TokenProgramMinttoCheckedInstruction(Instruction):
        amount: int
        decimals: int

        mint: Account
        account_to_mint: Account
        minting_authority: Account

    class TokenProgramBurnCheckedInstruction(Instruction):
        amount: int
        decimals: int

        account_to_burn_from: Account
        token_mint: Account
        owner: Account

    class TokenProgramInitializeAccount2Instruction(Instruction):
        owner: int

        account_to_initialize: Account
        mint_account: Account
        rent_sysvar: Account

    class TokenProgramSyncNativeInstruction(Instruction):

        token_account: Account

    class TokenProgramInitializeAccount3Instruction(Instruction):
        owner: int

        account_to_initialize: Account
        mint_account: Account

    class TokenProgramInitializeImmutableOwnerInstruction(Instruction):

        account_to_initialize: Account

    class Token2022ProgramInitializeAccountInstruction(Instruction):

        account_to_initialize: Account
        mint_account: Account
        owner: Account
        rent_sysvar: Account

    class Token2022ProgramInitializeMultisigInstruction(Instruction):
        number_of_signers: int

        multisig_account: Account
        rent_sysvar: Account
        signer_accounts: Account

    class Token2022ProgramTransferInstruction(Instruction):
        amount: int

        source_account: Account
        destination_account: Account
        owner: Account

    class Token2022ProgramApproveInstruction(Instruction):
        amount: int

        source_account: Account
        delegate_account: Account
        owner: Account

    class Token2022ProgramRevokeInstruction(Instruction):

        source_account: Account
        owner: Account

    class Token2022ProgramSetAuthorityInstruction(Instruction):
        authority_type: int
        new_authority: Account

        mint_account: Account
        current_authority: Account

    class Token2022ProgramMinttoInstruction(Instruction):
        amount: int

        mint: Account
        account_to_mint: Account
        minting_authority: Account

    class Token2022ProgramBurnInstruction(Instruction):
        amount: int

        account_to_burn_from: Account
        token_mint: Account
        owner: Account

    class Token2022ProgramCloseAccountInstruction(Instruction):

        account_to_close: Account
        destination_account: Account
        owner: Account

    class Token2022ProgramFreezeAccountInstruction(Instruction):

        account_to_freeze: Account
        token_mint: Account
        freeze_authority: Account

    class Token2022ProgramThawAccountInstruction(Instruction):

        account_to_freeze: Account
        token_mint: Account
        freeze_authority: Account

    class Token2022ProgramTransferCheckedInstruction(Instruction):
        amount: int
        decimals: int

        source_account: Account
        token_mint: Account
        destination_account: Account
        owner: Account

    class Token2022ProgramApproveCheckedInstruction(Instruction):
        amount: int
        decimals: int

        source_account: Account
        token_mint: Account
        delegate: Account
        owner: Account

    class Token2022ProgramMinttoCheckedInstruction(Instruction):
        amount: int
        decimals: int

        mint: Account
        account_to_mint: Account
        minting_authority: Account

    class Token2022ProgramBurnCheckedInstruction(Instruction):
        amount: int
        decimals: int

        account_to_burn_from: Account
        token_mint: Account
        owner: Account

    class Token2022ProgramInitializeAccount2Instruction(Instruction):
        owner: int

        account_to_initialize: Account
        mint_account: Account
        rent_sysvar: Account

    class Token2022ProgramSyncNativeInstruction(Instruction):

        token_account: Account

    class Token2022ProgramInitializeAccount3Instruction(Instruction):
        owner: int

        account_to_initialize: Account
        mint_account: Account

    class Token2022ProgramInitializeImmutableOwnerInstruction(Instruction):

        account_to_initialize: Account

    class AssociatedTokenAccountProgramCreateInstruction(Instruction):

        funding_account: Account
        associated_token_account: Account
        wallet_address: Account
        token_mint: Account
        system_program: Account
        spl_token: Account
        rent_sysvar: Account | None

    class AssociatedTokenAccountProgramCreateIdempotentInstruction(Instruction):

        funding_account: Account
        associated_token_account: Account
        wallet_addr: Account
        token_mint: Account
        system_program: Account
        spl_token: Account

    class AssociatedTokenAccountProgramRecoverNestedInstruction(Instruction):

        nested_account: Account
        token_mint_nested: Account
        associated_token_account: Account
        owner: Account
        token_mint_owner: Account
        wallet_address: Account
        spl_token: Account

    class MemoProgramMemoInstruction(Instruction):
        memo: str

        signer_accounts: Account | None

    class MemoLegacyProgramMemoInstruction(Instruction):
        memo: str

        signer_accounts: Account | None


def get_instruction_id_length(program_id: str) -> int:
    if program_id == _SYSTEM_PROGRAM_ID:
        return 4
    if program_id == _STAKE_PROGRAM_ID:
        return 4
    if program_id == _COMPUTE_BUDGET_PROGRAM_ID:
        return 1
    if program_id == _TOKEN_PROGRAM_ID:
        return 1
    if program_id == _TOKEN_2022_PROGRAM_ID:
        return 1
    if program_id == _ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID:
        return 1
    if program_id == _MEMO_PROGRAM_ID:
        return 0
    if program_id == _MEMO_LEGACY_PROGRAM_ID:
        return 0

    return 0


def format_StakeAuthorize(_: Instruction, value: int) -> str:
    if value == 0:
        return "Stake"
    if value == 1:
        return "Withdraw"
    raise DataError("Unknown value")


def format_AuthorityType(_: Instruction, value: int) -> str:
    if value == 0:
        return "Mint tokens"
    if value == 1:
        return "Freeze account"
    if value == 2:
        return "Account owner"
    if value == 3:
        return "Close account"
    raise DataError("Unknown value")


def get_instruction(
    program_id: str,
    instruction_id: InstructionId,
    instruction_accounts: list[Account],
    instruction_data: InstructionData,
) -> Instruction:
    if program_id == _SYSTEM_PROGRAM_ID:
        if instruction_id == _SYSTEM_PROGRAM_ID_INS_CREATE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _SYSTEM_PROGRAM_ID_INS_CREATE_ACCOUNT,
                [
                    PropertyTemplate(
                        "lamports",
                        False,
                        False,
                        read_uint64_le,
                        format_lamports,
                    ),
                    PropertyTemplate(
                        "space",
                        False,
                        False,
                        read_uint64_le,
                        format_int,
                    ),
                    PropertyTemplate(
                        "owner",
                        True,
                        False,
                        parse_pubkey,
                        format_pubkey,
                    ),
                ],
                [
                    AccountTemplate(
                        "funding_account",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "new_account",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "new_account",
                        "Create account",
                        False,
                        None,
                    ),
                    UIProperty(
                        "lamports",
                        None,
                        "Deposit",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "funding_account",
                        "From",
                        False,
                        None,
                    ),
                ],
                "System Program: Create Account",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _SYSTEM_PROGRAM_ID_INS_ASSIGN:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _SYSTEM_PROGRAM_ID_INS_ASSIGN,
                [
                    PropertyTemplate(
                        "owner",
                        True,
                        False,
                        parse_pubkey,
                        format_pubkey,
                    ),
                ],
                [
                    AccountTemplate(
                        "assigned_account",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "assigned_account",
                        "Assign account",
                        False,
                        None,
                    ),
                    UIProperty(
                        "owner",
                        None,
                        "Assign account to program",
                        False,
                        None,
                    ),
                ],
                "System Program: Assign",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _SYSTEM_PROGRAM_ID_INS_TRANSFER:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _SYSTEM_PROGRAM_ID_INS_TRANSFER,
                [
                    PropertyTemplate(
                        "lamports",
                        False,
                        False,
                        read_uint64_le,
                        format_lamports,
                    ),
                ],
                [
                    AccountTemplate(
                        "funding_account",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "recipient_account",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "recipient_account",
                        "Recipient",
                        False,
                        None,
                    ),
                    UIProperty(
                        "lamports",
                        None,
                        "Amount",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "funding_account",
                        "Sender",
                        False,
                        None,
                    ),
                ],
                "System Program: Transfer",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _SYSTEM_PROGRAM_ID_INS_CREATE_ACCOUNT_WITH_SEED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _SYSTEM_PROGRAM_ID_INS_CREATE_ACCOUNT_WITH_SEED,
                [
                    PropertyTemplate(
                        "base",
                        False,
                        False,
                        parse_pubkey,
                        format_pubkey,
                    ),
                    PropertyTemplate(
                        "seed",
                        False,
                        False,
                        parse_string,
                        format_identity,
                    ),
                    PropertyTemplate(
                        "lamports",
                        False,
                        False,
                        read_uint64_le,
                        format_lamports,
                    ),
                    PropertyTemplate(
                        "space",
                        False,
                        False,
                        read_uint64_le,
                        format_int,
                    ),
                    PropertyTemplate(
                        "owner",
                        False,
                        False,
                        parse_pubkey,
                        format_pubkey,
                    ),
                ],
                [
                    AccountTemplate(
                        "funding_account",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "created_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "base_account",
                        True,
                        True,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "created_account",
                        "Create account",
                        False,
                        None,
                    ),
                    UIProperty(
                        "lamports",
                        None,
                        "Deposit",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "funding_account",
                        "From",
                        False,
                        None,
                    ),
                ],
                "System Program: Create Account With Seed",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _SYSTEM_PROGRAM_ID_INS_ADVANCE_NONCE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _SYSTEM_PROGRAM_ID_INS_ADVANCE_NONCE_ACCOUNT,
                [],
                [
                    AccountTemplate(
                        "nonce_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "recent_blockhashes_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "nonce_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "nonce_account",
                        "Advance nonce",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "nonce_authority",
                        "Authorized by",
                        False,
                        None,
                    ),
                ],
                "System Program: Advance Nonce Account",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _SYSTEM_PROGRAM_ID_INS_WITHDRAW_NONCE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _SYSTEM_PROGRAM_ID_INS_WITHDRAW_NONCE_ACCOUNT,
                [
                    PropertyTemplate(
                        "lamports",
                        False,
                        False,
                        read_uint64_le,
                        format_lamports,
                    ),
                ],
                [
                    AccountTemplate(
                        "nonce_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "recipient_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "recent_blockhashes_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "rent_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "nonce_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "lamports",
                        None,
                        "Nonce withdraw",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "nonce_account",
                        "From",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "recipient_account",
                        "To",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "nonce_authority",
                        "Authorized by",
                        False,
                        None,
                    ),
                ],
                "System Program: Withdraw Nonce Account",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _SYSTEM_PROGRAM_ID_INS_INITIALIZE_NONCE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _SYSTEM_PROGRAM_ID_INS_INITIALIZE_NONCE_ACCOUNT,
                [
                    PropertyTemplate(
                        "nonce_authority",
                        True,
                        False,
                        parse_pubkey,
                        format_pubkey,
                    ),
                ],
                [
                    AccountTemplate(
                        "nonce_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "recent_blockhashes_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "rent_sysvar",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "nonce_account",
                        "Initialize nonce account",
                        False,
                        None,
                    ),
                    UIProperty(
                        "nonce_authority",
                        None,
                        "New authority",
                        False,
                        None,
                    ),
                ],
                "System Program: Initialize Nonce Account",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _SYSTEM_PROGRAM_ID_INS_AUTHORIZE_NONCE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _SYSTEM_PROGRAM_ID_INS_AUTHORIZE_NONCE_ACCOUNT,
                [
                    PropertyTemplate(
                        "nonce_authority",
                        True,
                        False,
                        parse_pubkey,
                        format_pubkey,
                    ),
                ],
                [
                    AccountTemplate(
                        "nonce_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "nonce_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "nonce_account",
                        "Set nonce authority",
                        False,
                        None,
                    ),
                    UIProperty(
                        "nonce_authority",
                        None,
                        "New authority",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "nonce_authority",
                        "Authorized by",
                        False,
                        None,
                    ),
                ],
                "System Program: Authorize Nonce Account",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _SYSTEM_PROGRAM_ID_INS_ALLOCATE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _SYSTEM_PROGRAM_ID_INS_ALLOCATE,
                [
                    PropertyTemplate(
                        "space",
                        False,
                        False,
                        read_uint64_le,
                        format_int,
                    ),
                ],
                [
                    AccountTemplate(
                        "new_account",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "new_account",
                        "Allocate account",
                        False,
                        None,
                    ),
                    UIProperty(
                        "space",
                        None,
                        "Data size",
                        False,
                        None,
                    ),
                ],
                "System Program: Allocate",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _SYSTEM_PROGRAM_ID_INS_ALLOCATE_WITH_SEED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _SYSTEM_PROGRAM_ID_INS_ALLOCATE_WITH_SEED,
                [
                    PropertyTemplate(
                        "base",
                        False,
                        False,
                        parse_pubkey,
                        format_pubkey,
                    ),
                    PropertyTemplate(
                        "seed",
                        False,
                        False,
                        parse_string,
                        format_identity,
                    ),
                    PropertyTemplate(
                        "space",
                        False,
                        False,
                        read_uint64_le,
                        format_int,
                    ),
                    PropertyTemplate(
                        "owner",
                        False,
                        False,
                        parse_pubkey,
                        format_pubkey,
                    ),
                ],
                [
                    AccountTemplate(
                        "allocated_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "base_account",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "allocated_account",
                        "Allocate data for account",
                        False,
                        None,
                    ),
                    UIProperty(
                        "space",
                        None,
                        "Data size",
                        False,
                        None,
                    ),
                ],
                "System Program: Allocate With Seed",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _SYSTEM_PROGRAM_ID_INS_ASSIGN_WITH_SEED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _SYSTEM_PROGRAM_ID_INS_ASSIGN_WITH_SEED,
                [
                    PropertyTemplate(
                        "base",
                        False,
                        False,
                        parse_pubkey,
                        format_pubkey,
                    ),
                    PropertyTemplate(
                        "seed",
                        False,
                        False,
                        parse_string,
                        format_identity,
                    ),
                    PropertyTemplate(
                        "owner",
                        False,
                        False,
                        parse_pubkey,
                        format_pubkey,
                    ),
                ],
                [
                    AccountTemplate(
                        "assigned_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "base_account",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "assigned_account",
                        "Assign account",
                        False,
                        None,
                    ),
                    UIProperty(
                        "owner",
                        None,
                        "Assign account to program",
                        False,
                        None,
                    ),
                ],
                "System Program: Assign With Seed",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _SYSTEM_PROGRAM_ID_INS_TRANSFER_WITH_SEED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _SYSTEM_PROGRAM_ID_INS_TRANSFER_WITH_SEED,
                [
                    PropertyTemplate(
                        "lamports",
                        False,
                        False,
                        read_uint64_le,
                        format_lamports,
                    ),
                    PropertyTemplate(
                        "from_seed",
                        False,
                        False,
                        parse_string,
                        format_identity,
                    ),
                    PropertyTemplate(
                        "from_owner",
                        False,
                        False,
                        parse_pubkey,
                        format_pubkey,
                    ),
                ],
                [
                    AccountTemplate(
                        "funding_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "base_account",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "recipient_account",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "recipient_account",
                        "Recipient",
                        False,
                        None,
                    ),
                    UIProperty(
                        "lamports",
                        None,
                        "Amount",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "funding_account",
                        "Sender",
                        False,
                        None,
                    ),
                ],
                "System Program: Transfer With Seed",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _SYSTEM_PROGRAM_ID_INS_UPGRADE_NONCE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _SYSTEM_PROGRAM_ID_INS_UPGRADE_NONCE_ACCOUNT,
                [],
                [
                    AccountTemplate(
                        "nonce_account",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "nonce_account",
                        "Upgrade nonce account",
                        False,
                        None,
                    ),
                ],
                "System Program: Upgrade Nonce Account",
                True,
                True,
                False,
                False,
                None,
            )
        return Instruction(
            instruction_data,
            program_id,
            instruction_accounts,
            instruction_id,
            [],
            [],
            [],
            "System Program",
            True,
            False,
            False,
            False,
        )
    if program_id == _STAKE_PROGRAM_ID:
        if instruction_id == _STAKE_PROGRAM_ID_INS_INITIALIZE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _STAKE_PROGRAM_ID_INS_INITIALIZE,
                [
                    PropertyTemplate(
                        "staker",
                        True,
                        False,
                        parse_pubkey,
                        format_pubkey,
                    ),
                    PropertyTemplate(
                        "withdrawer",
                        True,
                        False,
                        parse_pubkey,
                        format_pubkey,
                    ),
                    PropertyTemplate(
                        "unix_timestamp",
                        False,
                        False,
                        read_uint64_le,
                        format_unix_timestamp,
                    ),
                    PropertyTemplate(
                        "epoch",
                        False,
                        False,
                        read_uint64_le,
                        format_int,
                    ),
                    PropertyTemplate(
                        "custodian",
                        True,
                        False,
                        parse_pubkey,
                        format_pubkey,
                    ),
                ],
                [
                    AccountTemplate(
                        "uninitialized_stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "rent_sysvar",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "uninitialized_stake_account",
                        "Initialize stake account",
                        False,
                        None,
                    ),
                    UIProperty(
                        "staker",
                        None,
                        "New stake authority",
                        False,
                        None,
                    ),
                    UIProperty(
                        "withdrawer",
                        None,
                        "New withdraw authority",
                        False,
                        None,
                    ),
                    UIProperty(
                        "unix_timestamp",
                        None,
                        "Lockup time",
                        False,
                        0,
                    ),
                    UIProperty(
                        "epoch",
                        None,
                        "Lockup epoch",
                        False,
                        0,
                    ),
                    UIProperty(
                        "custodian",
                        None,
                        "Lockup authority",
                        False,
                        None,
                    ),
                ],
                "Stake Program: Initialize",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _STAKE_PROGRAM_ID_INS_AUTHORIZE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _STAKE_PROGRAM_ID_INS_AUTHORIZE,
                [
                    PropertyTemplate(
                        "pubkey",
                        False,
                        False,
                        parse_pubkey,
                        format_pubkey,
                    ),
                    PropertyTemplate(
                        "stake_authorize",
                        False,
                        False,
                        read_uint32_le,
                        format_StakeAuthorize,
                    ),
                ],
                [
                    AccountTemplate(
                        "stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "clock_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_or_withdraw_authority",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "lockup_authority",
                        True,
                        True,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "stake_account",
                        "Set authority for",
                        False,
                        None,
                    ),
                    UIProperty(
                        "pubkey",
                        None,
                        "New authority",
                        False,
                        None,
                    ),
                    UIProperty(
                        "stake_authorize",
                        None,
                        "Authority type",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "stake_or_withdraw_authority",
                        "Authorized by",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "lockup_authority",
                        "Custodian",
                        False,
                        None,
                    ),
                ],
                "Stake Program: Authorize",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _STAKE_PROGRAM_ID_INS_DELEGATE_STAKE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _STAKE_PROGRAM_ID_INS_DELEGATE_STAKE,
                [],
                [
                    AccountTemplate(
                        "initialized_stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "vote_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "clock_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_history_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "config_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "initialized_stake_account",
                        "Delegate from",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "stake_authority",
                        "Authorized by",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "vote_account",
                        "Vote account",
                        False,
                        None,
                    ),
                ],
                "Stake Program: Delegate Stake",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _STAKE_PROGRAM_ID_INS_SPLIT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _STAKE_PROGRAM_ID_INS_SPLIT,
                [
                    PropertyTemplate(
                        "lamports",
                        False,
                        False,
                        read_uint64_le,
                        format_lamports,
                    ),
                ],
                [
                    AccountTemplate(
                        "stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "uninitialized_stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "lamports",
                        None,
                        "Split stake",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "stake_account",
                        "From",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "uninitialized_stake_account",
                        "To",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "stake_authority",
                        "Authorized by",
                        False,
                        None,
                    ),
                ],
                "Stake Program: Split",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _STAKE_PROGRAM_ID_INS_WITHDRAW:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _STAKE_PROGRAM_ID_INS_WITHDRAW,
                [
                    PropertyTemplate(
                        "lamports",
                        False,
                        False,
                        read_uint64_le,
                        format_lamports,
                    ),
                ],
                [
                    AccountTemplate(
                        "stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "recipient_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "clock_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_history_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "withdrawal_authority",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "lockup_authority",
                        True,
                        True,
                    ),
                ],
                [
                    UIProperty(
                        "lamports",
                        None,
                        "Withdraw stake",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "stake_account",
                        "From",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "recipient_account",
                        "To",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "withdrawal_authority",
                        "Authorized by",
                        False,
                        None,
                    ),
                ],
                "Stake Program: Withdraw",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _STAKE_PROGRAM_ID_INS_DEACTIVATE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _STAKE_PROGRAM_ID_INS_DEACTIVATE,
                [],
                [
                    AccountTemplate(
                        "delegated_stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "clock_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "delegated_stake_account",
                        "Deactivate stake account",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "stake_authority",
                        "Authorized by",
                        False,
                        None,
                    ),
                ],
                "Stake Program: Deactivate",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _STAKE_PROGRAM_ID_INS_SET_LOCKUP:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _STAKE_PROGRAM_ID_INS_SET_LOCKUP,
                [
                    PropertyTemplate(
                        "unix_timestamp",
                        False,
                        True,
                        read_uint64_le,
                        format_unix_timestamp,
                    ),
                    PropertyTemplate(
                        "epoch",
                        False,
                        True,
                        read_uint64_le,
                        format_int,
                    ),
                    PropertyTemplate(
                        "custodian",
                        False,
                        True,
                        parse_pubkey,
                        format_pubkey,
                    ),
                ],
                [
                    AccountTemplate(
                        "initialized_stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "lockup_or_withdraw_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "initialized_stake_account",
                        "Set lockup for account",
                        False,
                        None,
                    ),
                    UIProperty(
                        "unix_timestamp",
                        None,
                        "Time",
                        False,
                        0,
                    ),
                    UIProperty(
                        "epoch",
                        None,
                        "Epoch",
                        False,
                        0,
                    ),
                    UIProperty(
                        "custodian",
                        None,
                        "New lockup authority",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "lockup_or_withdraw_authority",
                        "Authorized by",
                        False,
                        None,
                    ),
                ],
                "Stake Program: Set Lockup",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _STAKE_PROGRAM_ID_INS_MERGE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _STAKE_PROGRAM_ID_INS_MERGE,
                [],
                [
                    AccountTemplate(
                        "destination_stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "source_stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "clock_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_history_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "source_stake_account",
                        "Merge stake account",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "destination_stake_account",
                        "Into",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "stake_authority",
                        "Authorized by",
                        False,
                        None,
                    ),
                ],
                "Stake Program: Merge",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _STAKE_PROGRAM_ID_INS_AUTHORIZE_WITH_SEED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _STAKE_PROGRAM_ID_INS_AUTHORIZE_WITH_SEED,
                [
                    PropertyTemplate(
                        "new_authorized_pubkey",
                        False,
                        False,
                        parse_pubkey,
                        format_pubkey,
                    ),
                    PropertyTemplate(
                        "stake_authorize",
                        False,
                        False,
                        read_uint32_le,
                        format_StakeAuthorize,
                    ),
                    PropertyTemplate(
                        "authority_seed",
                        False,
                        False,
                        parse_string,
                        format_identity,
                    ),
                    PropertyTemplate(
                        "authority_owner",
                        False,
                        False,
                        parse_pubkey,
                        format_pubkey,
                    ),
                ],
                [
                    AccountTemplate(
                        "stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_or_withdraw_authority",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "clock_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "lockup_authority",
                        True,
                        True,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "stake_account",
                        "Set authority for",
                        False,
                        None,
                    ),
                    UIProperty(
                        "new_authorized_pubkey",
                        None,
                        "New authority",
                        False,
                        None,
                    ),
                    UIProperty(
                        "stake_authorize",
                        None,
                        "Authority type",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "stake_or_withdraw_authority",
                        "Authorized by",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "lockup_authority",
                        "Custodian",
                        False,
                        None,
                    ),
                ],
                "Stake Program: Authorize With Seed",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _STAKE_PROGRAM_ID_INS_INITIALIZE_CHECKED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _STAKE_PROGRAM_ID_INS_INITIALIZE_CHECKED,
                [],
                [
                    AccountTemplate(
                        "uninitialized_stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "rent_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_authority",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "withdrawal_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "uninitialized_stake_account",
                        "Uninitialized stake account",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "stake_authority",
                        "New stake authority",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "withdrawal_authority",
                        "New withdraw authority",
                        False,
                        None,
                    ),
                ],
                "Stake Program: Initialize Checked",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _STAKE_PROGRAM_ID_INS_AUTHORIZE_CHECKED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _STAKE_PROGRAM_ID_INS_AUTHORIZE_CHECKED,
                [
                    PropertyTemplate(
                        "stake_authorize",
                        False,
                        False,
                        read_uint32_le,
                        format_StakeAuthorize,
                    ),
                ],
                [
                    AccountTemplate(
                        "stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "clock_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_or_withdraw_authority",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "new_stake_or_withdraw_authority",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "lockup_authority",
                        True,
                        True,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "stake_account",
                        "Set authority for",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "new_stake_or_withdraw_authority",
                        "New authority",
                        False,
                        None,
                    ),
                    UIProperty(
                        "stake_authorize",
                        None,
                        "Authority type",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "stake_or_withdraw_authority",
                        "Authorized by",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "lockup_authority",
                        "Custodian",
                        False,
                        None,
                    ),
                ],
                "Stake Program: Authorize Checked",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _STAKE_PROGRAM_ID_INS_AUTHORIZE_CHECKED_WITH_SEED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _STAKE_PROGRAM_ID_INS_AUTHORIZE_CHECKED_WITH_SEED,
                [
                    PropertyTemplate(
                        "stake_authorize",
                        False,
                        False,
                        read_uint32_le,
                        format_StakeAuthorize,
                    ),
                    PropertyTemplate(
                        "authority_seed",
                        False,
                        False,
                        parse_string,
                        format_identity,
                    ),
                    PropertyTemplate(
                        "authority_owner",
                        False,
                        False,
                        parse_pubkey,
                        format_pubkey,
                    ),
                ],
                [
                    AccountTemplate(
                        "stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "stake_or_withdraw_authority",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "clock_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "new_stake_or_withdraw_authority",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "lockup_authority",
                        True,
                        True,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "stake_account",
                        "Set authority for",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "new_stake_or_withdraw_authority",
                        "New authority",
                        False,
                        None,
                    ),
                    UIProperty(
                        "stake_authorize",
                        None,
                        "Authority type",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "stake_or_withdraw_authority",
                        "Authorized by",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "lockup_authority",
                        "Custodian",
                        False,
                        None,
                    ),
                ],
                "Stake Program: Authorize Checked With Seed",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _STAKE_PROGRAM_ID_INS_SET_LOCKUP_CHECKED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _STAKE_PROGRAM_ID_INS_SET_LOCKUP_CHECKED,
                [
                    PropertyTemplate(
                        "unix_timestamp",
                        False,
                        True,
                        read_uint64_le,
                        format_unix_timestamp,
                    ),
                    PropertyTemplate(
                        "epoch",
                        False,
                        True,
                        read_uint64_le,
                        format_int,
                    ),
                ],
                [
                    AccountTemplate(
                        "stake_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "lockup_or_withdraw_authority",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "new_lockup_authority",
                        True,
                        True,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "stake_account",
                        "Set lockup for stake account",
                        False,
                        None,
                    ),
                    UIProperty(
                        "unix_timestamp",
                        None,
                        "Time",
                        False,
                        0,
                    ),
                    UIProperty(
                        "epoch",
                        None,
                        "Epoch",
                        False,
                        0,
                    ),
                    UIProperty(
                        None,
                        "new_lockup_authority",
                        "New lockup authority",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "lockup_or_withdraw_authority",
                        "Authorized by",
                        False,
                        None,
                    ),
                ],
                "Stake Program: Set Lockup Checked",
                True,
                True,
                False,
                False,
                None,
            )
        return Instruction(
            instruction_data,
            program_id,
            instruction_accounts,
            instruction_id,
            [],
            [],
            [],
            "Stake Program",
            True,
            False,
            False,
            False,
        )
    if program_id == _COMPUTE_BUDGET_PROGRAM_ID:
        if instruction_id == _COMPUTE_BUDGET_PROGRAM_ID_INS_REQUEST_HEAP_FRAME:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _COMPUTE_BUDGET_PROGRAM_ID_INS_REQUEST_HEAP_FRAME,
                [
                    PropertyTemplate(
                        "bytes",
                        False,
                        False,
                        read_uint32_le,
                        format_int,
                    ),
                ],
                [],
                [
                    UIProperty(
                        "bytes",
                        None,
                        "Bytes",
                        False,
                        None,
                    ),
                ],
                "Compute Budget Program: Request Heap Frame",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _COMPUTE_BUDGET_PROGRAM_ID_INS_SET_COMPUTE_UNIT_LIMIT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _COMPUTE_BUDGET_PROGRAM_ID_INS_SET_COMPUTE_UNIT_LIMIT,
                [
                    PropertyTemplate(
                        "units",
                        False,
                        False,
                        read_uint32_le,
                        format_int,
                    ),
                ],
                [],
                [
                    UIProperty(
                        "units",
                        None,
                        "Units",
                        False,
                        None,
                    ),
                ],
                "Compute Budget Program: Set Compute Unit Limit",
                True,
                True,
                True,
                False,
                None,
            )
        if instruction_id == _COMPUTE_BUDGET_PROGRAM_ID_INS_SET_COMPUTE_UNIT_PRICE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _COMPUTE_BUDGET_PROGRAM_ID_INS_SET_COMPUTE_UNIT_PRICE,
                [
                    PropertyTemplate(
                        "lamports",
                        False,
                        False,
                        read_uint64_le,
                        format_int,
                    ),
                ],
                [],
                [
                    UIProperty(
                        "lamports",
                        None,
                        "Compute unit price",
                        False,
                        None,
                    ),
                ],
                "Compute Budget Program: Set Compute Unit Price",
                True,
                True,
                True,
                False,
                None,
            )
        return Instruction(
            instruction_data,
            program_id,
            instruction_accounts,
            instruction_id,
            [],
            [],
            [],
            "Compute Budget Program",
            True,
            False,
            False,
            False,
        )
    if program_id == _TOKEN_PROGRAM_ID:
        if instruction_id == _TOKEN_PROGRAM_ID_INS_INITIALIZE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_PROGRAM_ID_INS_INITIALIZE_ACCOUNT,
                [],
                [
                    AccountTemplate(
                        "account_to_initialize",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "mint_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "rent_sysvar",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_initialize",
                        "Initialize account",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "mint_account",
                        "For token",
                        False,
                        None,
                    ),
                ],
                "Token Program: Initialize Account",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _TOKEN_PROGRAM_ID_INS_INITIALIZE_MULTISIG:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_PROGRAM_ID_INS_INITIALIZE_MULTISIG,
                [
                    PropertyTemplate(
                        "number_of_signers",
                        False,
                        False,
                        parse_byte,
                        format_int,
                    ),
                ],
                [
                    AccountTemplate(
                        "multisig_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "rent_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "signer_accounts",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "multisig_account",
                        "Initialize multisig",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "signer_accounts",
                        "Required signers",
                        False,
                        None,
                    ),
                ],
                "Token Program: Initialize Multisig",
                True,
                True,
                False,
                True,
                None,
            )
        if instruction_id == _TOKEN_PROGRAM_ID_INS_TRANSFER:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_PROGRAM_ID_INS_TRANSFER,
                [
                    PropertyTemplate(
                        "amount",
                        False,
                        False,
                        read_uint64_le,
                        format_int,
                    ),
                ],
                [
                    AccountTemplate(
                        "source_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "destination_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "destination_account",
                        "Recipient",
                        False,
                        None,
                    ),
                    UIProperty(
                        "amount",
                        None,
                        "Amount",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "source_account",
                        "From",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                        None,
                    ),
                ],
                "Token Program: Transfer",
                True,
                True,
                False,
                True,
                "Warning: Instruction is deprecated. Token decimals unknown.",
            )
        if instruction_id == _TOKEN_PROGRAM_ID_INS_APPROVE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_PROGRAM_ID_INS_APPROVE,
                [
                    PropertyTemplate(
                        "amount",
                        False,
                        False,
                        read_uint64_le,
                        format_int,
                    ),
                ],
                [
                    AccountTemplate(
                        "source_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "delegate_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "delegate_account",
                        "Approve delegate",
                        False,
                        None,
                    ),
                    UIProperty(
                        "amount",
                        None,
                        "Allowance",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                        None,
                    ),
                ],
                "Token Program: Approve",
                True,
                True,
                False,
                True,
                "Warning: Instruction is deprecated. Token decimals unknown.",
            )
        if instruction_id == _TOKEN_PROGRAM_ID_INS_REVOKE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_PROGRAM_ID_INS_REVOKE,
                [],
                [
                    AccountTemplate(
                        "source_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "source_account",
                        "Revoke delegate",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                        None,
                    ),
                ],
                "Token Program: Revoke",
                True,
                True,
                False,
                True,
                None,
            )
        if instruction_id == _TOKEN_PROGRAM_ID_INS_SET_AUTHORITY:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_PROGRAM_ID_INS_SET_AUTHORITY,
                [
                    PropertyTemplate(
                        "authority_type",
                        False,
                        False,
                        parse_byte,
                        format_AuthorityType,
                    ),
                    PropertyTemplate(
                        "new_authority",
                        True,
                        True,
                        parse_pubkey,
                        format_pubkey,
                    ),
                ],
                [
                    AccountTemplate(
                        "mint_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "current_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "mint_account",
                        "Set authority for",
                        False,
                        None,
                    ),
                    UIProperty(
                        "new_authority",
                        None,
                        "New authority",
                        False,
                        None,
                    ),
                    UIProperty(
                        "authority_type",
                        None,
                        "Authority type",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "current_authority",
                        "Current authority",
                        False,
                        None,
                    ),
                ],
                "Token Program: Set Authority",
                True,
                True,
                False,
                True,
                None,
            )
        if instruction_id == _TOKEN_PROGRAM_ID_INS_MINT_TO:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_PROGRAM_ID_INS_MINT_TO,
                [
                    PropertyTemplate(
                        "amount",
                        False,
                        False,
                        read_uint64_le,
                        format_int,
                    ),
                ],
                [
                    AccountTemplate(
                        "mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "account_to_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "minting_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "amount",
                        None,
                        "Mint tokens",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "account_to_mint",
                        "To",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "minting_authority",
                        "Mint authority",
                        False,
                        None,
                    ),
                ],
                "Token Program: Mint To",
                True,
                True,
                False,
                True,
                "Warning: Instruction is deprecated. Token decimals unknown.",
            )
        if instruction_id == _TOKEN_PROGRAM_ID_INS_BURN:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_PROGRAM_ID_INS_BURN,
                [
                    PropertyTemplate(
                        "amount",
                        False,
                        False,
                        read_uint64_le,
                        format_int,
                    ),
                ],
                [
                    AccountTemplate(
                        "account_to_burn_from",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "amount",
                        None,
                        "Burn tokens",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "account_to_burn_from",
                        "From",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Mint authority",
                        False,
                        None,
                    ),
                ],
                "Token Program: Burn",
                True,
                True,
                False,
                True,
                "Warning: Instruction is deprecated. Token decimals unknown.",
            )
        if instruction_id == _TOKEN_PROGRAM_ID_INS_CLOSE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_PROGRAM_ID_INS_CLOSE_ACCOUNT,
                [],
                [
                    AccountTemplate(
                        "account_to_close",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "destination_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_close",
                        "Close account",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "destination_account",
                        "Withdraw to",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                        None,
                    ),
                ],
                "Token Program: Close Account",
                True,
                True,
                False,
                True,
                None,
            )
        if instruction_id == _TOKEN_PROGRAM_ID_INS_FREEZE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_PROGRAM_ID_INS_FREEZE_ACCOUNT,
                [],
                [
                    AccountTemplate(
                        "account_to_freeze",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "freeze_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_freeze",
                        "Freeze account",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "freeze_authority",
                        "Owner",
                        False,
                        None,
                    ),
                ],
                "Token Program: Freeze Account",
                True,
                True,
                False,
                True,
                None,
            )
        if instruction_id == _TOKEN_PROGRAM_ID_INS_THAW_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_PROGRAM_ID_INS_THAW_ACCOUNT,
                [],
                [
                    AccountTemplate(
                        "account_to_freeze",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "freeze_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_freeze",
                        "Thaw account",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "freeze_authority",
                        "Owner",
                        False,
                        None,
                    ),
                ],
                "Token Program: Thaw Account",
                True,
                True,
                False,
                True,
                None,
            )
        if instruction_id == _TOKEN_PROGRAM_ID_INS_TRANSFER_CHECKED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_PROGRAM_ID_INS_TRANSFER_CHECKED,
                [
                    PropertyTemplate(
                        "amount",
                        False,
                        False,
                        read_uint64_le,
                        format_token_amount,
                    ),
                    PropertyTemplate(
                        "decimals",
                        False,
                        False,
                        parse_byte,
                        format_int,
                    ),
                ],
                [
                    AccountTemplate(
                        "source_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "destination_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "token_mint",
                        "Token",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "destination_account",
                        "Recipient",
                        False,
                        None,
                    ),
                    UIProperty(
                        "amount",
                        None,
                        "Amount",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "source_account",
                        "From",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                        None,
                    ),
                ],
                "Token Program: Transfer Checked",
                True,
                True,
                False,
                True,
                None,
            )
        if instruction_id == _TOKEN_PROGRAM_ID_INS_APPROVE_CHECKED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_PROGRAM_ID_INS_APPROVE_CHECKED,
                [
                    PropertyTemplate(
                        "amount",
                        False,
                        False,
                        read_uint64_le,
                        format_token_amount,
                    ),
                    PropertyTemplate(
                        "decimals",
                        False,
                        False,
                        parse_byte,
                        format_int,
                    ),
                ],
                [
                    AccountTemplate(
                        "source_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "delegate",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "token_mint",
                        "Approve token",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "delegate",
                        "Approve delegate",
                        False,
                        None,
                    ),
                    UIProperty(
                        "amount",
                        None,
                        "Allowance",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "source_account",
                        "From",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                        None,
                    ),
                ],
                "Token Program: Approve Checked",
                True,
                True,
                False,
                True,
                None,
            )
        if instruction_id == _TOKEN_PROGRAM_ID_INS_MINT_TO_CHECKED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_PROGRAM_ID_INS_MINT_TO_CHECKED,
                [
                    PropertyTemplate(
                        "amount",
                        False,
                        False,
                        read_uint64_le,
                        format_token_amount,
                    ),
                    PropertyTemplate(
                        "decimals",
                        False,
                        False,
                        parse_byte,
                        format_int,
                    ),
                ],
                [
                    AccountTemplate(
                        "mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "account_to_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "minting_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "mint",
                        "Mint token",
                        False,
                        None,
                    ),
                    UIProperty(
                        "amount",
                        None,
                        "Mint amount",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "account_to_mint",
                        "To",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "minting_authority",
                        "Owner",
                        False,
                        None,
                    ),
                ],
                "Token Program: Mint to Checked",
                True,
                True,
                False,
                True,
                None,
            )
        if instruction_id == _TOKEN_PROGRAM_ID_INS_BURN_CHECKED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_PROGRAM_ID_INS_BURN_CHECKED,
                [
                    PropertyTemplate(
                        "amount",
                        False,
                        False,
                        read_uint64_le,
                        format_token_amount,
                    ),
                    PropertyTemplate(
                        "decimals",
                        False,
                        False,
                        parse_byte,
                        format_int,
                    ),
                ],
                [
                    AccountTemplate(
                        "account_to_burn_from",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "token_mint",
                        "Burn token",
                        False,
                        None,
                    ),
                    UIProperty(
                        "amount",
                        None,
                        "Burn amount",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "account_to_burn_from",
                        "From",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                        None,
                    ),
                ],
                "Token Program: Burn Checked",
                True,
                True,
                False,
                True,
                None,
            )
        if instruction_id == _TOKEN_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_2:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_2,
                [
                    PropertyTemplate(
                        "owner",
                        False,
                        False,
                        parse_pubkey,
                        format_pubkey,
                    ),
                ],
                [
                    AccountTemplate(
                        "account_to_initialize",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "mint_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "rent_sysvar",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_initialize",
                        "Initialize account",
                        False,
                        None,
                    ),
                    UIProperty(
                        "owner",
                        None,
                        "Owner",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "mint_account",
                        "For token",
                        False,
                        None,
                    ),
                ],
                "Token Program: Initialize Account 2",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _TOKEN_PROGRAM_ID_INS_SYNC_NATIVE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_PROGRAM_ID_INS_SYNC_NATIVE,
                [],
                [
                    AccountTemplate(
                        "token_account",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "token_account",
                        "Sync native account",
                        False,
                        None,
                    ),
                ],
                "Token Program: Sync Native",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _TOKEN_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_3:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_3,
                [
                    PropertyTemplate(
                        "owner",
                        False,
                        False,
                        parse_pubkey,
                        format_pubkey,
                    ),
                ],
                [
                    AccountTemplate(
                        "account_to_initialize",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "mint_account",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_initialize",
                        "Initialize account",
                        False,
                        None,
                    ),
                    UIProperty(
                        "owner",
                        None,
                        "Owner",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "mint_account",
                        "For token",
                        False,
                        None,
                    ),
                ],
                "Token Program: Initialize Account 3",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _TOKEN_PROGRAM_ID_INS_INITIALIZE_IMMUTABLE_OWNER:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_PROGRAM_ID_INS_INITIALIZE_IMMUTABLE_OWNER,
                [],
                [
                    AccountTemplate(
                        "account_to_initialize",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_initialize",
                        "Init account",
                        False,
                        None,
                    ),
                ],
                "Token Program: Initialize Immutable Owner",
                True,
                True,
                False,
                False,
                None,
            )
        return Instruction(
            instruction_data,
            program_id,
            instruction_accounts,
            instruction_id,
            [],
            [],
            [],
            "Token Program",
            True,
            False,
            False,
            False,
        )
    if program_id == _TOKEN_2022_PROGRAM_ID:
        if instruction_id == _TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_ACCOUNT,
                [],
                [
                    AccountTemplate(
                        "account_to_initialize",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "mint_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "rent_sysvar",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_initialize",
                        "Initialize account",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "mint_account",
                        "For token",
                        False,
                        None,
                    ),
                ],
                "Token 2022 Program: Initialize Account",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_MULTISIG:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_MULTISIG,
                [
                    PropertyTemplate(
                        "number_of_signers",
                        False,
                        False,
                        parse_byte,
                        format_int,
                    ),
                ],
                [
                    AccountTemplate(
                        "multisig_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "rent_sysvar",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "signer_accounts",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "multisig_account",
                        "Init multisig",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "signer_accounts",
                        "Required signers",
                        False,
                        None,
                    ),
                ],
                "Token 2022 Program: Initialize Multisig",
                True,
                True,
                False,
                True,
                None,
            )
        if instruction_id == _TOKEN_2022_PROGRAM_ID_INS_TRANSFER:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_2022_PROGRAM_ID_INS_TRANSFER,
                [
                    PropertyTemplate(
                        "amount",
                        False,
                        False,
                        read_uint64_le,
                        format_int,
                    ),
                ],
                [
                    AccountTemplate(
                        "source_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "destination_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "destination_account",
                        "Recipient",
                        False,
                        None,
                    ),
                    UIProperty(
                        "amount",
                        None,
                        "Amount",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "source_account",
                        "From",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                        None,
                    ),
                ],
                "Token 2022 Program: Transfer",
                True,
                True,
                False,
                True,
                "Warning: Instruction is deprecated. Token decimals unknown.",
            )
        if instruction_id == _TOKEN_2022_PROGRAM_ID_INS_APPROVE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_2022_PROGRAM_ID_INS_APPROVE,
                [
                    PropertyTemplate(
                        "amount",
                        False,
                        False,
                        read_uint64_le,
                        format_int,
                    ),
                ],
                [
                    AccountTemplate(
                        "source_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "delegate_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "delegate_account",
                        "Approve delegate",
                        False,
                        None,
                    ),
                    UIProperty(
                        "amount",
                        None,
                        "Allowance",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                        None,
                    ),
                ],
                "Token 2022 Program: Approve",
                True,
                True,
                False,
                True,
                "Warning: Instruction is deprecated. Token decimals unknown.",
            )
        if instruction_id == _TOKEN_2022_PROGRAM_ID_INS_REVOKE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_2022_PROGRAM_ID_INS_REVOKE,
                [],
                [
                    AccountTemplate(
                        "source_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "source_account",
                        "Rewoke delegate",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                        None,
                    ),
                ],
                "Token 2022 Program: Revoke",
                True,
                True,
                False,
                True,
                None,
            )
        if instruction_id == _TOKEN_2022_PROGRAM_ID_INS_SET_AUTHORITY:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_2022_PROGRAM_ID_INS_SET_AUTHORITY,
                [
                    PropertyTemplate(
                        "authority_type",
                        False,
                        False,
                        parse_byte,
                        format_AuthorityType,
                    ),
                    PropertyTemplate(
                        "new_authority",
                        True,
                        True,
                        parse_pubkey,
                        format_pubkey,
                    ),
                ],
                [
                    AccountTemplate(
                        "mint_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "current_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "mint_account",
                        "Set authority for",
                        False,
                        None,
                    ),
                    UIProperty(
                        "new_authority",
                        None,
                        "New authority",
                        False,
                        None,
                    ),
                    UIProperty(
                        "authority_type",
                        None,
                        "Authority type",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "current_authority",
                        "Current authority",
                        False,
                        None,
                    ),
                ],
                "Token 2022 Program: Set Authority",
                True,
                True,
                False,
                True,
                None,
            )
        if instruction_id == _TOKEN_2022_PROGRAM_ID_INS_MINT_TO:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_2022_PROGRAM_ID_INS_MINT_TO,
                [
                    PropertyTemplate(
                        "amount",
                        False,
                        False,
                        read_uint64_le,
                        format_int,
                    ),
                ],
                [
                    AccountTemplate(
                        "mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "account_to_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "minting_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "amount",
                        None,
                        "Mint tokens",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "account_to_mint",
                        "To",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "minting_authority",
                        "Mint authority",
                        False,
                        None,
                    ),
                ],
                "Token 2022 Program: Mint to",
                True,
                True,
                False,
                True,
                "Warning: Instruction is deprecated. Token decimals unknown.",
            )
        if instruction_id == _TOKEN_2022_PROGRAM_ID_INS_BURN:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_2022_PROGRAM_ID_INS_BURN,
                [
                    PropertyTemplate(
                        "amount",
                        False,
                        False,
                        read_uint64_le,
                        format_int,
                    ),
                ],
                [
                    AccountTemplate(
                        "account_to_burn_from",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        "amount",
                        None,
                        "Burn tokens",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "account_to_burn_from",
                        "From",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Mint authority",
                        False,
                        None,
                    ),
                ],
                "Token 2022 Program: Burn",
                True,
                True,
                False,
                True,
                "Warning: Instruction is deprecated. Token decimals unknown.",
            )
        if instruction_id == _TOKEN_2022_PROGRAM_ID_INS_CLOSE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_2022_PROGRAM_ID_INS_CLOSE_ACCOUNT,
                [],
                [
                    AccountTemplate(
                        "account_to_close",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "destination_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_close",
                        "Close account",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "destination_account",
                        "Withdraw to",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                        None,
                    ),
                ],
                "Token 2022 Program: Close Account",
                True,
                True,
                False,
                True,
                None,
            )
        if instruction_id == _TOKEN_2022_PROGRAM_ID_INS_FREEZE_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_2022_PROGRAM_ID_INS_FREEZE_ACCOUNT,
                [],
                [
                    AccountTemplate(
                        "account_to_freeze",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "freeze_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_freeze",
                        "Freeze account",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "freeze_authority",
                        "Owner",
                        False,
                        None,
                    ),
                ],
                "Token 2022 Program: Freeze Account",
                True,
                True,
                False,
                True,
                None,
            )
        if instruction_id == _TOKEN_2022_PROGRAM_ID_INS_THAW_ACCOUNT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_2022_PROGRAM_ID_INS_THAW_ACCOUNT,
                [],
                [
                    AccountTemplate(
                        "account_to_freeze",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "freeze_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_freeze",
                        "Thaw account",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "freeze_authority",
                        "Owner",
                        False,
                        None,
                    ),
                ],
                "Token 2022 Program: Thaw Account",
                True,
                True,
                False,
                True,
                None,
            )
        if instruction_id == _TOKEN_2022_PROGRAM_ID_INS_TRANSFER_CHECKED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_2022_PROGRAM_ID_INS_TRANSFER_CHECKED,
                [
                    PropertyTemplate(
                        "amount",
                        False,
                        False,
                        read_uint64_le,
                        format_token_amount,
                    ),
                    PropertyTemplate(
                        "decimals",
                        False,
                        False,
                        parse_byte,
                        format_int,
                    ),
                ],
                [
                    AccountTemplate(
                        "source_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "destination_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "token_mint",
                        "Token",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "destination_account",
                        "Recipient",
                        False,
                        None,
                    ),
                    UIProperty(
                        "amount",
                        None,
                        "Amount",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "source_account",
                        "From",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                        None,
                    ),
                ],
                "Token 2022 Program: Transfer Checked",
                True,
                True,
                False,
                True,
                None,
            )
        if instruction_id == _TOKEN_2022_PROGRAM_ID_INS_APPROVE_CHECKED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_2022_PROGRAM_ID_INS_APPROVE_CHECKED,
                [
                    PropertyTemplate(
                        "amount",
                        False,
                        False,
                        read_uint64_le,
                        format_token_amount,
                    ),
                    PropertyTemplate(
                        "decimals",
                        False,
                        False,
                        parse_byte,
                        format_int,
                    ),
                ],
                [
                    AccountTemplate(
                        "source_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "delegate",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "token_mint",
                        "Approve token",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "delegate",
                        "Approve delegate",
                        False,
                        None,
                    ),
                    UIProperty(
                        "amount",
                        None,
                        "Allowance",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "source_account",
                        "From",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                        None,
                    ),
                ],
                "Token 2022 Program: Approve Checked",
                True,
                True,
                False,
                True,
                None,
            )
        if instruction_id == _TOKEN_2022_PROGRAM_ID_INS_MINT_TO_CHECKED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_2022_PROGRAM_ID_INS_MINT_TO_CHECKED,
                [
                    PropertyTemplate(
                        "amount",
                        False,
                        False,
                        read_uint64_le,
                        format_token_amount,
                    ),
                    PropertyTemplate(
                        "decimals",
                        False,
                        False,
                        parse_byte,
                        format_int,
                    ),
                ],
                [
                    AccountTemplate(
                        "mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "account_to_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "minting_authority",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "mint",
                        "Mint token",
                        False,
                        None,
                    ),
                    UIProperty(
                        "amount",
                        None,
                        "Mint amount",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "account_to_mint",
                        "To",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "minting_authority",
                        "Owner",
                        False,
                        None,
                    ),
                ],
                "Token 2022 Program: Mint to Checked",
                True,
                True,
                False,
                True,
                None,
            )
        if instruction_id == _TOKEN_2022_PROGRAM_ID_INS_BURN_CHECKED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_2022_PROGRAM_ID_INS_BURN_CHECKED,
                [
                    PropertyTemplate(
                        "amount",
                        False,
                        False,
                        read_uint64_le,
                        format_token_amount,
                    ),
                    PropertyTemplate(
                        "decimals",
                        False,
                        False,
                        parse_byte,
                        format_int,
                    ),
                ],
                [
                    AccountTemplate(
                        "account_to_burn_from",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        True,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "token_mint",
                        "Burn token",
                        False,
                        None,
                    ),
                    UIProperty(
                        "amount",
                        None,
                        "Burn amount",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "account_to_burn_from",
                        "From",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "owner",
                        "Owner",
                        False,
                        None,
                    ),
                ],
                "Token 2022 Program: Burn Checked",
                True,
                True,
                False,
                True,
                None,
            )
        if instruction_id == _TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_2:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_2,
                [
                    PropertyTemplate(
                        "owner",
                        False,
                        False,
                        parse_pubkey,
                        format_pubkey,
                    ),
                ],
                [
                    AccountTemplate(
                        "account_to_initialize",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "mint_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "rent_sysvar",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_initialize",
                        "Initialize account",
                        False,
                        None,
                    ),
                    UIProperty(
                        "owner",
                        None,
                        "Owner",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "mint_account",
                        "For token",
                        False,
                        None,
                    ),
                ],
                "Token 2022 Program: Initialize Account 2",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _TOKEN_2022_PROGRAM_ID_INS_SYNC_NATIVE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_2022_PROGRAM_ID_INS_SYNC_NATIVE,
                [],
                [
                    AccountTemplate(
                        "token_account",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "token_account",
                        "Sync native account",
                        False,
                        None,
                    ),
                ],
                "Token 2022 Program: Sync Native",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_3:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_ACCOUNT_3,
                [
                    PropertyTemplate(
                        "owner",
                        False,
                        False,
                        parse_pubkey,
                        format_pubkey,
                    ),
                ],
                [
                    AccountTemplate(
                        "account_to_initialize",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "mint_account",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_initialize",
                        "Initialize account",
                        False,
                        None,
                    ),
                    UIProperty(
                        "owner",
                        None,
                        "Owner",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "mint_account",
                        "For token",
                        False,
                        None,
                    ),
                ],
                "Token 2022 Program: Initialize Account 3",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_IMMUTABLE_OWNER:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _TOKEN_2022_PROGRAM_ID_INS_INITIALIZE_IMMUTABLE_OWNER,
                [],
                [
                    AccountTemplate(
                        "account_to_initialize",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "account_to_initialize",
                        "Initialize immutable owner extension for account",
                        False,
                        None,
                    ),
                ],
                "Token 2022 Program: Initialize Immutable Owner",
                True,
                True,
                False,
                False,
                None,
            )
        return Instruction(
            instruction_data,
            program_id,
            instruction_accounts,
            instruction_id,
            [],
            [],
            [],
            "Token 2022 Program",
            True,
            False,
            False,
            False,
        )
    if program_id == _ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID:
        if instruction_id == _ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID_INS_CREATE:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID_INS_CREATE,
                [],
                [
                    AccountTemplate(
                        "funding_account",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "associated_token_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "wallet_address",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "system_program",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "spl_token",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "rent_sysvar",
                        False,
                        True,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "associated_token_account",
                        "Create token account",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "token_mint",
                        "For token",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "wallet_address",
                        "Owned by",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "funding_account",
                        "Funded by",
                        False,
                        None,
                    ),
                ],
                "Associated Token Account Program: Create",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID_INS_CREATE_IDEMPOTENT:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID_INS_CREATE_IDEMPOTENT,
                [],
                [
                    AccountTemplate(
                        "funding_account",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "associated_token_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "wallet_addr",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "system_program",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "spl_token",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "associated_token_account",
                        "Create token account",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "token_mint",
                        "For token",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "wallet_addr",
                        "Owned by",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "funding_account",
                        "Funded by",
                        False,
                        None,
                    ),
                ],
                "Associated Token Account Program: Create Idempotent",
                True,
                True,
                False,
                False,
                None,
            )
        if instruction_id == _ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID_INS_RECOVER_NESTED:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _ASSOCIATED_TOKEN_ACCOUNT_PROGRAM_ID_INS_RECOVER_NESTED,
                [],
                [
                    AccountTemplate(
                        "nested_account",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint_nested",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "associated_token_account",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "owner",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "token_mint_owner",
                        False,
                        False,
                    ),
                    AccountTemplate(
                        "wallet_address",
                        True,
                        False,
                    ),
                    AccountTemplate(
                        "spl_token",
                        False,
                        False,
                    ),
                ],
                [
                    UIProperty(
                        None,
                        "nested_account",
                        "Recover nested token account",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "associated_token_account",
                        "Transfer recovered tokens to",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "wallet_address",
                        "Transfer recovered SOL to",
                        False,
                        None,
                    ),
                ],
                "Associated Token Account Program: Recover Nested",
                True,
                True,
                False,
                False,
                None,
            )
        return Instruction(
            instruction_data,
            program_id,
            instruction_accounts,
            instruction_id,
            [],
            [],
            [],
            "Associated Token Account Program",
            True,
            False,
            False,
            False,
        )
    if program_id == _MEMO_PROGRAM_ID:
        if instruction_id == _MEMO_PROGRAM_ID_INS_MEMO:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _MEMO_PROGRAM_ID_INS_MEMO,
                [
                    PropertyTemplate(
                        "memo",
                        False,
                        False,
                        parse_memo,
                        format_identity,
                    ),
                ],
                [
                    AccountTemplate(
                        "signer_accounts",
                        True,
                        True,
                    ),
                ],
                [
                    UIProperty(
                        "memo",
                        None,
                        "Memo",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "signer_accounts",
                        "Signer accounts",
                        False,
                        None,
                    ),
                ],
                "Memo Program: Memo",
                True,
                True,
                False,
                False,
                None,
            )
        return Instruction(
            instruction_data,
            program_id,
            instruction_accounts,
            instruction_id,
            [],
            [],
            [],
            "Memo Program",
            True,
            False,
            False,
            False,
        )
    if program_id == _MEMO_LEGACY_PROGRAM_ID:
        if instruction_id == _MEMO_LEGACY_PROGRAM_ID_INS_MEMO:
            return Instruction(
                instruction_data,
                program_id,
                instruction_accounts,
                _MEMO_LEGACY_PROGRAM_ID_INS_MEMO,
                [
                    PropertyTemplate(
                        "memo",
                        False,
                        False,
                        parse_memo,
                        format_identity,
                    ),
                ],
                [
                    AccountTemplate(
                        "signer_accounts",
                        True,
                        True,
                    ),
                ],
                [
                    UIProperty(
                        "memo",
                        None,
                        "Memo",
                        False,
                        None,
                    ),
                    UIProperty(
                        None,
                        "signer_accounts",
                        "Signer accounts",
                        False,
                        None,
                    ),
                ],
                "Memo Legacy Program: Memo",
                True,
                True,
                False,
                False,
                None,
            )
        return Instruction(
            instruction_data,
            program_id,
            instruction_accounts,
            instruction_id,
            [],
            [],
            [],
            "Memo Legacy Program",
            True,
            False,
            False,
            False,
        )
    return Instruction(
        instruction_data,
        program_id,
        instruction_accounts,
        0,
        [],
        [],
        [],
        "Unsupported program",
        False,
        False,
        False,
        False,
    )
