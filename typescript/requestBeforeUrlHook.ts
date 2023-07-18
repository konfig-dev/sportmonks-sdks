import { RequestArgs } from "./base";
import { Configuration } from "./configuration";

export function requestBeforeUrlHook(request: {
  axiosArgs: RequestArgs;
  basePath: string;
  configuration?: Configuration;
}): void {
  request.axiosArgs.url = request.axiosArgs.url.replace(
    "-version-",
    request.configuration.version
  );
  request.axiosArgs.url = request.axiosArgs.url.replace(
    "-sport-",
    request.configuration.sport
  );
}
