/*
 * This file is part of the Trezor project, https://trezor.io/
 *
 * Copyright (c) SatoshiLabs
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <trezor_bsp.h>  // required by #ifdef STM32U5 below (see #4306 issue)
#include <trezor_rtl.h>

#include <rtl/cli.h>
#include <util/cpuid.h>

static void prodtest_get_cpuid(cli_t* cli) {
  if (cli_arg_count(cli) > 0) {
    cli_error_arg_count(cli);
    return;
  }

  cpuid_t cpuid = {0};

  cpuid_get(&cpuid);

  cli_ok_hexdata(cli, &cpuid.id, sizeof(cpuid.id));
}

// clang-format off

PRODTEST_CLI_CMD(
  .name = "get-cpuid",
  .func = prodtest_get_cpuid,
  .info = "Retrieve unique CPU ID",
  .args = ""
);


